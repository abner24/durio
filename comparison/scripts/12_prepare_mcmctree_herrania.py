#!/usr/bin/env python3
"""Add Herrania umbratica to the 300-gene MCMCtree alignment.

Blast each cacao (or T2T) single-copy sequence against the Herrania proteome,
add the best hit, realign with MAFFT --add, concatenate, write a calibrated
tree with cacao–Herrania 5–20 Ma and cacao-lineage vs Durio 60–90 Ma.
"""
from __future__ import annotations

import gzip
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cluster_paths import (
    CACAO_HERRANIA_LOWER,
    CACAO_HERRANIA_UPPER,
    ENV,
    HERRANIA,
    HERRANIA_PROTEIN_URL,
    MCMC_DIR,
    MCMC_TAXA,
    MCMC_TAXA_HERRANIA,
    MSA_DIR,
    OUTGROUP,
    PUBLIC_DIR,
    ROOT_LOWER_100MA,
    ROOT_UPPER_100MA,
)


def parse_fasta(path: Path) -> dict[str, str]:
    recs: dict[str, str] = {}
    hdr, seq = None, []
    gz = str(path).endswith(".gz")
    ctx = gzip.open(path, "rt") if gz else path.open()
    with ctx as fh:
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


def species_from_header(header: str) -> str | None:
    h = header.split()[0]
    for sp in (*MCMC_TAXA, HERRANIA):
        if h == sp or h.startswith(sp + "|") or h.startswith(sp + "_"):
            return sp
    if h.startswith("Thecc.") or h.startswith("Theobroma"):
        return OUTGROUP
    return None


def msa_to_taxa(recs: dict[str, str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for h, s in recs.items():
        sp = species_from_header(h)
        if sp in MCMC_TAXA:
            out[sp] = s.upper().replace("*", "X")
    return out


def write_fasta(path: Path, recs: dict[str, str]) -> None:
    with path.open("w") as fh:
        for k, v in recs.items():
            fh.write(f">{k}\n")
            for i in range(0, len(v), 80):
                fh.write(v[i : i + 80] + "\n")


def write_phylip(path: Path, alns: dict[str, str], order: tuple[str, ...]) -> None:
    n = len(order)
    l = len(alns[order[0]])
    with path.open("w") as fh:
        fh.write(f" {n} {l}\n")
        for t in order:
            fh.write(f"{t}\n")
            s = alns[t]
            for i in range(0, len(s), 60):
                fh.write(s[i : i + 60] + "\n")


def ensure_herrania_faa() -> Path:
    d = PUBLIC_DIR / "herrania"
    d.mkdir(parents=True, exist_ok=True)
    existing = list(d.glob("*.faa")) + list(d.glob("*.faa.gz")) + list(d.glob("*protein*.faa*"))
    for p in existing:
        if p.stat().st_size > 1000:
            if p.suffix == ".gz":
                out = d / "Herrania_umbratica.faa"
                if not out.exists():
                    out.write_text(gzip.open(p, "rt").read())
                return out
            return p
    gz = d / "Herrania_umbratica.faa.gz"
    print(f"[INFO] downloading Herrania proteome → {gz}")
    urllib.request.urlretrieve(HERRANIA_PROTEIN_URL, gz)
    out = d / "Herrania_umbratica.faa"
    out.write_text(gzip.open(gz, "rt").read())
    return out


def which_bin(name: str) -> str | None:
    p = shutil.which(name)
    if p:
        return p
    cand = ENV / "bin" / name
    return str(cand) if cand.exists() else None


def diamond_besthit(queries: Path, db_faa: Path, out_tsv: Path) -> dict[str, str]:
    diamond = which_bin("diamond")
    db = db_faa.with_suffix("")
    if diamond:
        subprocess.run(
            [diamond, "makedb", "--in", str(db_faa), "-d", str(db)],
            check=True,
        )
        subprocess.run(
            [
                diamond,
                "blastp",
                "-q",
                str(queries),
                "-d",
                str(db),
                "-o",
                str(out_tsv),
                "--outfmt",
                "6",
                "--max-target-seqs",
                "1",
                "--evalue",
                "1e-5",
                "-p",
                "8",
            ],
            check=True,
        )
    else:
        blastp = which_bin("blastp")
        makeblastdb = which_bin("makeblastdb")
        if not blastp or not makeblastdb:
            raise SystemExit("Need diamond or blastp in PATH / durio_evol")
        subprocess.run(
            [makeblastdb, "-in", str(db_faa), "-dbtype", "prot", "-out", str(db)],
            check=True,
        )
        subprocess.run(
            [
                blastp,
                "-query",
                str(queries),
                "-db",
                str(db),
                "-out",
                str(out_tsv),
                "-outfmt",
                "6",
                "-max_target_seqs",
                "1",
                "-evalue",
                "1e-5",
                "-num_threads",
                "8",
            ],
            check=True,
        )
    hits = {}
    for line in out_tsv.read_text().splitlines():
        q, s, *rest = line.split("\t")
        hits[q] = s
    return hits


def mafft_add(base_msa: Path, extra_fa: Path, out_fa: Path) -> None:
    mafft = which_bin("mafft")
    if not mafft:
        raise SystemExit("mafft not found")
    with out_fa.open("w") as fh:
        subprocess.run(
            [mafft, "--add", str(extra_fa), "--quiet", str(base_msa)],
            check=True,
            stdout=fh,
        )


def write_ctl(path: Path, seqfile: str, treefile: str, usedata: int) -> None:
    ud = f"{usedata} in.BV" if usedata == 2 else str(usedata)
    path.write_text(
        f"""seed = 1
seqfile = {seqfile}
treefile = {treefile}
outfile = out.txt

ndata = 1
seqtype = 2
usedata = {ud}
clock = 2
RootAge = 'B({ROOT_LOWER_100MA},{ROOT_UPPER_100MA})'
model = 2
aaRatefile = wag.dat
alpha = 0.5
ncatG = 4
cleandata = 0
BDparas = 1 1 0.1 C
kappa_gamma = 6 2
alpha_gamma = 1 1
rgene_gamma = 2 20
sigma2_gamma = 1 10
print = 1
burnin = 20000
sampfreq = 10
nsample = 40000
"""
    )


def main() -> None:
    out = MCMC_DIR / "herrania"
    inp = out / "input"
    prior = out / "prior"
    post = out / "posterior"
    tmp = out / "tmp"
    for d in (inp, prior, post, tmp):
        d.mkdir(parents=True, exist_ok=True)

    her_faa = ensure_herrania_faa()
    her_prot = parse_fasta(her_faa)
    print(f"[OK] Herrania proteins {len(her_prot)} from {her_faa}")

    used = MCMC_DIR / "input" / "used_ogs.txt"
    if not used.exists():
        raise SystemExit(f"Missing {used} — run the original MCMCtree prepare first")
    ogs = [ln.strip() for ln in used.read_text().splitlines() if ln.strip()]

    queries: dict[str, str] = {}
    msa_by_og: dict[str, dict[str, str]] = {}
    for og in ogs:
        p = MSA_DIR / f"{og}.fa"
        if not p.exists():
            continue
        alns = msa_to_taxa(parse_fasta(p))
        if any(t not in alns for t in MCMC_TAXA):
            continue
        msa_by_og[og] = alns
        qseq = alns[OUTGROUP].replace("-", "")
        if len(qseq) >= 50:
            queries[og] = qseq

    qfa = tmp / "cacao_queries.faa"
    write_fasta(qfa, queries)
    hits = diamond_besthit(qfa, her_faa, tmp / "herrania_hits.tsv")
    print(f"[OK] Herrania hits {len(hits)}/{len(queries)}")

    mafft = which_bin("mafft")
    concat = {t: [] for t in MCMC_TAXA_HERRANIA}
    kept = []
    skip = {"nohit": 0, "mafft": 0}
    for og, alns in msa_by_og.items():
        hid = hits.get(og)
        if not hid or hid not in her_prot:
            skip["nohit"] += 1
            continue
        base = tmp / f"{og}.msa.fa"
        extra = tmp / f"{og}.her.fa"
        added = tmp / f"{og}.add.fa"
        write_fasta(base, alns)
        write_fasta(extra, {HERRANIA: her_prot[hid]})
        try:
            if mafft:
                mafft_add(base, extra, added)
                new = parse_fasta(added)
            else:
                skip["mafft"] += 1
                continue
        except subprocess.CalledProcessError:
            skip["mafft"] += 1
            continue
        mapped = {}
        for h, s in new.items():
            sp = species_from_header(h) or (HERRANIA if h == HERRANIA else None)
            if sp:
                mapped[sp] = s.upper().replace("*", "X")
        if any(t not in mapped for t in MCMC_TAXA_HERRANIA):
            skip["mafft"] += 1
            continue
        L = len(mapped[OUTGROUP])
        if any(len(mapped[t]) != L for t in MCMC_TAXA_HERRANIA):
            skip["mafft"] += 1
            continue
        for t in MCMC_TAXA_HERRANIA:
            concat[t].append(mapped[t])
        kept.append(og)

    if len(kept) < 50:
        raise SystemExit(f"Too few genes after adding Herrania: {len(kept)}")
    concat = {t: "".join(concat[t]) for t in MCMC_TAXA_HERRANIA}
    write_phylip(inp / "concat.phy", concat, MCMC_TAXA_HERRANIA)
    write_fasta(inp / "concat.fa", concat)
    (inp / "used_ogs.txt").write_text("\n".join(kept) + "\n")

    durio = (
        "((DurSin,DurTes),(DurBru,(DurOxl,((DurDul,DurKut),"
        "(DurGra_Og,T2T_MK_mat)))))"
    )
    cal = (
        f"(({HERRANIA}, {OUTGROUP}) 'B({CACAO_HERRANIA_LOWER},{CACAO_HERRANIA_UPPER})', "
        f"{durio}) 'B({ROOT_LOWER_100MA},{ROOT_UPPER_100MA})';"
    )
    (inp / "species.tree").write_text(f"{len(MCMC_TAXA_HERRANIA)} 1\n{cal}\n")
    (inp / "species_uncalibrated.nwk").write_text(
        f"(({HERRANIA},{OUTGROUP}),{durio});\n"
    )

    write_ctl(prior / "mcmctree.ctl", "../input/concat.phy", "../input/species.tree", 0)
    write_ctl(post / "mcmctree.ctl", "../input/concat.phy", "../input/species.tree", 3)

    wag_src = MCMC_DIR / "input" / "wag.dat"
    if wag_src.exists():
        for dest in (inp, prior, post):
            shutil.copy(wag_src, dest / "wag.dat")
    else:
        found = list(ENV.rglob("wag.dat"))
        if not found:
            raise SystemExit("wag.dat not found")
        for dest in (inp, prior, post):
            shutil.copy(found[0], dest / "wag.dat")

    meta = {
        "n_input_ogs": len(ogs),
        "n_with_herrania": len(kept),
        "concat_aa": len(concat[OUTGROUP]),
        "taxa": list(MCMC_TAXA_HERRANIA),
        "skip": skip,
        "tree": cal,
        "herrania_proteome": str(her_faa),
        "calibrations": {
            "root_cacaoLineage_vs_Durio_Ma": [60, 90],
            "Theobroma_Herrania_Ma": [5, 20],
        },
    }
    (inp / "prepare_summary.json").write_text(json.dumps(meta, indent=2) + "\n")
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
