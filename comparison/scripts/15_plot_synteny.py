#!/usr/bin/env python3
"""Diamond reciprocal hits → collinear blocks → JCVI + matplotlib figures."""
from __future__ import annotations

import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.path import Path as MPath
import numpy as np

from cluster_paths import ENV, JCVI_DIR, JCVI_PAIRS, KARYOTYPE_TRACKS


def which_bin(name: str) -> str | None:
    p = shutil.which(name)
    if p:
        return p
    c = ENV / "bin" / name
    return str(c) if c.exists() else None


def load_bed(path: Path) -> dict[str, tuple[str, int, int, str]]:
    """gene -> (chrom, start, end, strand)"""
    out = {}
    with path.open() as fh:
        for line in fh:
            chrom, start, end, gid, _sc, strand = line.rstrip().split("\t")[:6]
            out[gid] = (chrom, int(start), int(end), strand)
    return out


def chrom_order(bed: dict[str, tuple[str, int, int, str]], seqids: list[str] | None):
    lens: dict[str, int] = defaultdict(int)
    for chrom, start, end, _s in bed.values():
        lens[chrom] = max(lens[chrom], end)
    if seqids:
        keep = [c for c in seqids if c in lens]
        rest = sorted((c for c in lens if c not in keep), key=lambda x: -lens[x])
        order = keep + rest
    else:
        order = sorted(lens, key=lambda x: -lens[x])
    offset = {}
    x = 0
    gap = 2_000_000
    for c in order[:28]:
        offset[c] = x
        x += lens[c] + gap
    return offset, lens, x


def diamond_pair(a: str, b: str, inp: Path, outd: Path, threads: int = 8) -> Path:
    diamond = which_bin("diamond")
    if not diamond:
        raise SystemExit("diamond not found")
    q, db = inp / f"{a}.pep", inp / f"{b}.pep"
    dbp = outd / f"{b}.dmnd"
    tsv = outd / f"{a}.{b}.blast"
    subprocess.run([diamond, "makedb", "--in", str(db), "-d", str(dbp)], check=True)
    subprocess.run(
        [
            diamond,
            "blastp",
            "-q",
            str(q),
            "-d",
            str(dbp),
            "-o",
            str(tsv),
            "--outfmt",
            "6",
            "--max-target-seqs",
            "5",
            "--evalue",
            "1e-5",
            "-p",
            str(threads),
        ],
        check=True,
    )
    return tsv


def reciprocal_best(fwd: Path, rev: Path) -> list[tuple[str, str, float]]:
    def best(path: Path) -> dict[str, tuple[str, float]]:
        hit = {}
        for line in path.read_text().splitlines():
            q, s, ident, *rest = line.split("\t")
            bits = float(rest[-1]) if rest else float(ident)
            if q not in hit or bits > hit[q][1]:
                hit[q] = (s, bits)
        return hit

    f, r = best(fwd), best(rev)
    pairs = []
    for q, (s, bits) in f.items():
        if r.get(s, (None, 0))[0] == q:
            pairs.append((q, s, bits))
    return pairs


def collinear_blocks(
    pairs: list[tuple[str, str, float]],
    bed_a: dict,
    bed_b: dict,
    min_size: int = 5,
) -> list[list[tuple[str, str]]]:
    # rank genes along each chrom
    rank_a: dict[str, int] = {}
    rank_b: dict[str, int] = {}
    by_chr_a: dict[str, list] = defaultdict(list)
    by_chr_b: dict[str, list] = defaultdict(list)
    for g, (c, s, e, st) in bed_a.items():
        by_chr_a[c].append((s, g))
    for g, (c, s, e, st) in bed_b.items():
        by_chr_b[c].append((s, g))
    for c, lst in by_chr_a.items():
        for i, (_s, g) in enumerate(sorted(lst)):
            rank_a[g] = i
    for c, lst in by_chr_b.items():
        for i, (_s, g) in enumerate(sorted(lst)):
            rank_b[g] = i

    grouped: dict[tuple[str, str], list] = defaultdict(list)
    for ga, gb, bits in pairs:
        if ga not in bed_a or gb not in bed_b:
            continue
        ca, cb = bed_a[ga][0], bed_b[gb][0]
        grouped[(ca, cb)].append((rank_a[ga], rank_b[gb], ga, gb, bits))

    blocks = []
    for (_ca, _cb), hits in grouped.items():
        hits.sort()
        used = set()
        for i, (ra, rb, ga, gb, _b) in enumerate(hits):
            if i in used:
                continue
            chain = [(ga, gb)]
            used.add(i)
            pra, prb = ra, rb
            for j in range(i + 1, len(hits)):
                if j in used:
                    continue
                r2a, r2b, g2a, g2b, _ = hits[j]
                if 0 < r2a - pra <= 20 and abs(r2b - prb) <= 20:
                    chain.append((g2a, g2b))
                    used.add(j)
                    pra, prb = r2a, r2b
            if len(chain) >= min_size:
                blocks.append(chain)
    return blocks


def write_anchors(path: Path, pairs: list[tuple[str, str, float]]) -> None:
    with path.open("w") as fh:
        for a, b, sc in pairs:
            fh.write(f"{a}\t{b}\t{sc:.1f}\n")


def write_simple(path: Path, blocks: list[list[tuple[str, str]]], bed_a, bed_b) -> None:
    with path.open("w") as fh:
        for i, bl in enumerate(blocks):
            a0, b0 = bl[0]
            a1, b1 = bl[-1]
            fh.write(
                f"{bed_a[a0][0]}:{bed_a[a0][1]}-{bed_a[a1][2]}\t"
                f"{bed_b[b0][0]}:{bed_b[b0][1]}-{bed_b[b1][2]}\t{len(bl)}\n"
            )


def ribbon(ax, x0, x1, y0, y1, color, alpha=0.35):
    verts = [
        (x0, y0),
        (x0, y0),
        ((x0 + x1) / 2, (y0 + y1) / 2),
        (x1, y1),
        (x1, y1),
        ((x0 + x1) / 2, (y0 + y1) / 2),
        (x0, y0),
    ]
    codes = [
        MPath.MOVETO,
        MPath.CURVE4,
        MPath.CURVE4,
        MPath.CURVE4,
        MPath.LINETO,
        MPath.CURVE4,
        MPath.CURVE4,
    ]
    # simpler polygon
    xm = (x0 + x1) / 2
    path = MPath(
        [(x0, y0), (xm, (y0 + y1) / 2), (x1, y1), (x1, y1), (xm, (y0 + y1) / 2), (x0, y0)],
        [MPath.MOVETO, MPath.CURVE3, MPath.CURVE3, MPath.LINETO, MPath.CURVE3, MPath.CURVE3],
    )
    ax.add_patch(PathPatch(path, facecolor=color, edgecolor="none", alpha=alpha))


def plot_dual(a, b, blocks, bed_a, bed_b, seq_a, seq_b, out_pdf: Path) -> None:
    off_a, lens_a, tot_a = chrom_order(bed_a, seq_a)
    off_b, lens_b, tot_b = chrom_order(bed_b, seq_b)
    fig, ax = plt.subplots(figsize=(14, 5))
    y_a, y_b = 0.72, 0.28
    for c, x in off_a.items():
        ax.add_patch(
            FancyBboxPatch(
                (x, y_a - 0.03),
                lens_a[c],
                0.06,
                boxstyle="round,pad=0.002",
                facecolor="#4c78a8",
                edgecolor="none",
            )
        )
    for c, x in off_b.items():
        ax.add_patch(
            FancyBboxPatch(
                (x, y_b - 0.03),
                lens_b[c],
                0.06,
                boxstyle="round,pad=0.002",
                facecolor="#f58518",
                edgecolor="none",
            )
        )
    cmap = plt.cm.tab20(np.linspace(0, 1, max(len(blocks), 1)))
    for i, bl in enumerate(blocks):
        ga0, gb0 = bl[0]
        ga1, gb1 = bl[-1]
        ca, sa, ea, _ = bed_a[ga0]
        ca2, sa2, ea2, _ = bed_a[ga1]
        cb, sb, eb, _ = bed_b[gb0]
        cb2, sb2, eb2, _ = bed_b[gb1]
        if ca not in off_a or cb not in off_b:
            continue
        x0 = off_a[ca] + (sa + ea2) / 2
        x1 = off_b[cb] + (sb + eb2) / 2
        ribbon(ax, x0, x1, y_a, y_b, cmap[i % len(cmap)])
    ax.set_xlim(0, max(tot_a, tot_b))
    ax.set_ylim(0.1, 0.9)
    ax.axis("off")
    ax.set_title(f"{a}  vs  {b}  ({len(blocks)} syntenic blocks)")
    ax.text(0, y_a + 0.08, a, fontsize=11)
    ax.text(0, y_b - 0.10, b, fontsize=11)
    fig.tight_layout()
    fig.savefig(out_pdf, dpi=150)
    fig.savefig(out_pdf.with_suffix(".png"), dpi=150)
    plt.close(fig)


def plot_dot(a, b, pairs, bed_a, bed_b, seq_a, seq_b, out_pdf: Path) -> None:
    off_a, lens_a, tot_a = chrom_order(bed_a, seq_a)
    off_b, lens_b, tot_b = chrom_order(bed_b, seq_b)
    xs, ys = [], []
    for ga, gb, _sc in pairs:
        if ga not in bed_a or gb not in bed_b:
            continue
        ca, sa, ea, _ = bed_a[ga]
        cb, sb, eb, _ = bed_b[gb]
        if ca not in off_a or cb not in off_b:
            continue
        xs.append(off_a[ca] + (sa + ea) / 2)
        ys.append(off_b[cb] + (sb + eb) / 2)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(xs, ys, s=2, c="#4c78a8", alpha=0.35, linewidths=0)
    ax.set_xlabel(a)
    ax.set_ylabel(b)
    ax.set_title(f"{a} vs {b} ({len(xs)} RBH)")
    fig.tight_layout()
    fig.savefig(out_pdf, dpi=150)
    fig.savefig(out_pdf.with_suffix(".png"), dpi=150)
    plt.close(fig)


def try_jcvi(inp: Path, outd: Path, a: str, b: str) -> None:
    py = which_bin("python") or sys.executable
    try:
        subprocess.run(
            [
                py,
                "-m",
                "jcvi.graphics.dotplot",
                str(outd / f"{a}.{b}.anchors"),
                "--outfile",
                str(outd / f"{a}.{b}.jcvi.dotplot.pdf"),
            ],
            check=True,
            cwd=str(inp),
            timeout=300,
        )
    except Exception as e:
        print(f"[WARN] jcvi.graphics.dotplot skipped: {e}")
    try:
        layout = inp / f"{a}.{b}.layout"
        layout.write_text(
            f"# y, xstart, xend, rotation, color, label, va, bed\n"
            f".6, .1, .8, 0, , {a}, top, {a}.bed\n"
            f".4, .1, .8, 0, , {b}, top, {b}.bed\n"
            f"# edges\n"
            f"e, 0, 1, {a}.{b}.anchors.simple\n"
        )
        subprocess.run(
            [
                py,
                "-m",
                "jcvi.graphics.synteny",
                str(outd / f"{a}.{b}.anchors.simple"),
                str(inp / f"{a}.bed"),
                str(inp / f"{b}.bed"),
                str(layout),
                "--outfile",
                str(outd / f"{a}.{b}.jcvi.synteny.pdf"),
            ],
            check=True,
            cwd=str(inp),
            timeout=300,
        )
    except Exception as e:
        print(f"[WARN] jcvi.graphics.synteny skipped: {e}")


def try_jcvi_karyotype(inp: Path, outd: Path) -> None:
    py = which_bin("python") or sys.executable
    try:
        subprocess.run(
            [
                py,
                "-m",
                "jcvi.graphics.karyotype",
                str(inp / "karyotype.seqids"),
                str(inp / "karyotype.layout"),
                "--outfile",
                str(outd / "karyotype.jcvi.pdf"),
            ],
            check=True,
            cwd=str(inp),
            timeout=600,
        )
    except Exception as e:
        print(f"[WARN] jcvi karyotype skipped: {e}")


def read_seqids(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [x for x in path.read_text().strip().split(",") if x]


def main() -> None:
    inp = JCVI_DIR / "input"
    outd = JCVI_DIR / "out"
    outd.mkdir(parents=True, exist_ok=True)
    threads = 8
    for a, b in JCVI_PAIRS:
        print(f"[INFO] pair {a} vs {b}")
        bed_a = load_bed(inp / f"{a}.bed")
        bed_b = load_bed(inp / f"{b}.bed")
        fwd = diamond_pair(a, b, inp, outd, threads)
        rev = diamond_pair(b, a, inp, outd, threads)
        pairs = reciprocal_best(fwd, rev)
        write_anchors(outd / f"{a}.{b}.anchors", pairs)
        # copy anchors next to beds for jcvi
        shutil.copy(outd / f"{a}.{b}.anchors", inp / f"{a}.{b}.anchors")
        blocks = collinear_blocks(pairs, bed_a, bed_b)
        write_simple(outd / f"{a}.{b}.anchors.simple", blocks, bed_a, bed_b)
        shutil.copy(outd / f"{a}.{b}.anchors.simple", inp / f"{a}.{b}.anchors.simple")
        seq_a = read_seqids(inp / f"{a}.seqids")
        seq_b = read_seqids(inp / f"{b}.seqids")
        plot_dual(a, b, blocks, bed_a, bed_b, seq_a, seq_b, outd / f"{a}.{b}.synteny.pdf")
        plot_dot(a, b, pairs, bed_a, bed_b, seq_a, seq_b, outd / f"{a}.{b}.dotplot.pdf")
        try_jcvi(inp, outd, a, b)
        print(f"[OK] {a}-{b}: {len(pairs)} RBH, {len(blocks)} blocks")
    try_jcvi_karyotype(inp, outd)
    print("[DONE] figures in", outd)


if __name__ == "__main__":
    main()
