#!/usr/bin/env python3
"""Prepare JCVI/MCScan inputs: per-genome BED + peptide FASTA with matching IDs.

Uses BRAKER GTF + comparison/01_proteomes/*.faa (and T2T GTF). Longest 28
scaffolds are written to seqids for karyotype plots.
"""
from __future__ import annotations

import gzip
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cluster_paths import (
    GENOME_FASTA,
    JCVI_DIR,
    JCVI_PAIRS,
    KARYOTYPE_TRACKS,
    gtf_paths,
    proteome_faa,
)


def parse_fasta(path: Path) -> dict[str, str]:
    recs: dict[str, str] = {}
    hdr, seq = None, []
    opener = gzip.open if str(path).endswith(".gz") else path.open
    with opener("rt") if str(path).endswith(".gz") else opener() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if hdr is not None:
                    recs[hdr] = "".join(seq)
                hdr = line[1:].split()[0]
                seq = []
            else:
                seq.append(line.replace(" ", ""))
        if hdr is not None:
            recs[hdr] = "".join(seq)
    return recs


def strip_sp(header: str, sample: str) -> str:
    h = header.split()[0]
    for prefix in (sample + "|", sample + "_"):
        if h.startswith(prefix):
            return h[len(prefix) :]
    return h


def parse_gtf(path: Path) -> list[tuple[str, int, int, str, str]]:
    """Return (chrom, start0, end, name, strand) for transcript/mRNA/gene."""
    rows = []
    with path.open() as fh:
        for line in fh:
            if not line.strip() or line.startswith("#"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 9:
                continue
            chrom, _src, typ, start, end, _sc, strand, _fr, attrs = p
            if typ not in {"transcript", "mRNA", "gene"}:
                continue
            name = None
            for kv in attrs.strip().strip(";").split(";"):
                kv = kv.strip()
                if not kv:
                    continue
                if " " in kv:
                    k, v = kv.split(" ", 1)
                elif "=" in kv:
                    k, v = kv.split("=", 1)
                else:
                    continue
                v = v.strip().strip('"')
                if k in {"transcript_id", "ID", "gene_id"}:
                    name = v
                    if k == "transcript_id":
                        break
            if not name:
                continue
            rows.append((chrom, int(start) - 1, int(end), name, strand))
    # prefer transcripts: if both gene and transcript, keep transcript-sized
    by_name: dict[str, tuple[str, int, int, str, str]] = {}
    for r in rows:
        prev = by_name.get(r[3])
        if prev is None or (r[2] - r[1]) >= (prev[2] - prev[1]):
            by_name[r[3]] = r
    return list(by_name.values())


def fasta_lengths(path: Path) -> dict[str, int]:
    lens: dict[str, int] = {}
    n, cur = None, 0
    with path.open() as fh:
        for line in fh:
            if line.startswith(">"):
                if n is not None:
                    lens[n] = cur
                n = line[1:].split()[0]
                cur = 0
            else:
                cur += len(line.strip())
        if n is not None:
            lens[n] = cur
    return lens


def find_gtf(sample: str) -> Path:
    for p in gtf_paths(sample):
        if p.exists():
            return p
    raise FileNotFoundError(f"No GTF for {sample}: {gtf_paths(sample)}")


def write_bed_pep(sample: str, outdir: Path) -> dict:
    gtf = find_gtf(sample)
    faa_p = proteome_faa(sample)
    if not faa_p.exists():
        raise FileNotFoundError(faa_p)
    genome = GENOME_FASTA[sample]
    feats = parse_gtf(gtf)
    pep = parse_fasta(faa_p)
    pep_by_short = {strip_sp(k, sample): v for k, v in pep.items()}
    # also index without .t1
    extra = {}
    for k, v in pep_by_short.items():
        extra[k.split(".")[0]] = v
        extra[k] = v

    bed_rows = []
    pep_out = {}
    for chrom, start, end, name, strand in feats:
        key = None
        for cand in (name, name.split(".")[0], strip_sp(name, sample)):
            if cand in pep_by_short:
                key = cand
                break
            if cand in extra:
                key = cand
                break
        if key is None:
            continue
        gid = key.replace("|", "_")
        bed_rows.append((chrom, start, end, gid, strand))
        pep_out[gid] = extra.get(key, pep_by_short.get(key, ""))

    bed_p = outdir / f"{sample}.bed"
    pep_p = outdir / f"{sample}.pep"
    with bed_p.open("w") as fh:
        for chrom, start, end, gid, strand in sorted(bed_rows, key=lambda x: (x[0], x[1])):
            fh.write(f"{chrom}\t{start}\t{end}\t{gid}\t0\t{strand}\n")
    with pep_p.open("w") as fh:
        for gid, seq in pep_out.items():
            if not seq:
                continue
            fh.write(f">{gid}\n")
            for i in range(0, len(seq), 80):
                fh.write(seq[i : i + 80] + "\n")

    seqids = []
    if genome.exists():
        lens = fasta_lengths(genome)
        top = sorted(lens.items(), key=lambda kv: -kv[1])[:28]
        seqids = [c for c, _ in top]
    (outdir / f"{sample}.seqids").write_text(",".join(seqids) + "\n")
    return {
        "sample": sample,
        "gtf": str(gtf),
        "bed": str(bed_p),
        "pep": str(pep_p),
        "n_bed": len(bed_rows),
        "n_pep": len(pep_out),
        "n_seqids": len(seqids),
    }


def write_karyotype_layout(outdir: Path) -> None:
    # jcvi karyotype layout
    lines = ["# y, xstart, xend, rotation, color, label, va, bed"]
    ys = [0.75, 0.55, 0.35, 0.15]
    for y, sp in zip(ys, KARYOTYPE_TRACKS):
        lines.append(f"{y:.2f}, .08, .92, 0, , {sp}, top, {sp}.bed")
    lines.append("# edges")
    for i in range(len(KARYOTYPE_TRACKS) - 1):
        a, b = KARYOTYPE_TRACKS[i], KARYOTYPE_TRACKS[i + 1]
        lines.append(f"e, {i}, {i+1}, {a}.{b}.anchors.simple")
    (outdir / "karyotype.layout").write_text("\n".join(lines) + "\n")
    seq_lines = []
    for sp in KARYOTYPE_TRACKS:
        p = outdir / f"{sp}.seqids"
        seq_lines.append(p.read_text().strip() if p.exists() else "")
    (outdir / "karyotype.seqids").write_text("\n".join(seq_lines) + "\n")


def main() -> None:
    out = JCVI_DIR / "input"
    out.mkdir(parents=True, exist_ok=True)
    samples = sorted({s for pair in JCVI_PAIRS for s in pair} | set(KARYOTYPE_TRACKS))
    report = []
    for sp in samples:
        try:
            rec = write_bed_pep(sp, out)
            report.append(rec)
            print(f"[OK] {sp} bed={rec['n_bed']} pep={rec['n_pep']}")
        except Exception as e:
            print(f"[ERR] {sp}: {e}")
            report.append({"sample": sp, "error": str(e)})
    write_karyotype_layout(out)
    import json

    (out / "prepare_summary.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
