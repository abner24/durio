#!/usr/bin/env python3
"""Walk assembly/<species>/ and write ASSEMBLY_QC_INVENTORY.md (run from repo or any cwd)."""
from __future__ import annotations

import datetime as _dt
import glob
import re
from pathlib import Path


ASSEMBLY_ROOT = Path("/home/proj_202504p2_BD-MED/abner/durio/assembly")
OUT_PATH = ASSEMBLY_ROOT / "ASSEMBLY_QC_INVENTORY.md"


def human_size(n: int) -> str:
    x = float(n)
    for u in ("B", "KiB", "MiB", "GiB", "TiB"):
        if x < 1024 or u == "TiB":
            if u == "B":
                return f"{int(x)} B"
            return f"{x:.2f} {u}"
        x /= 1024
    return f"{n} B"


def stat_line(p: Path) -> tuple[str, str]:
    if not p.is_file():
        return ("—", "—")
    st = p.stat()
    m = _dt.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")
    return (human_size(st.st_size), m)


def first_file(pattern: str) -> Path | None:
    hits = sorted(glob.glob(pattern))
    return Path(hits[0]) if hits else None


def find_one(root: Path, patterns: list[str]) -> Path | None:
    if not root.exists():
        return None
    for pat in patterns:
        try:
            for hit in sorted(root.glob(pat)):
                if hit.is_file():
                    return hit
        except (ValueError, OSError):
            continue
    return None


def find_busco_full_table(sp: Path, stage: str) -> Path | None:
    d = sp / f"results/qc/busco/{stage}"
    if not d.is_dir():
        return None
    hits = sorted(d.rglob("full_table.tsv"))
    return hits[0] if hits else None


def find_busco_short_summary(sp: Path, stage: str) -> Path | None:
    d = sp / f"results/qc/busco/{stage}"
    if not d.is_dir():
        return None
    hits = sorted(d.glob("short_summary*.txt"))
    return hits[0] if hits else None


def parse_input_yaml(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    m = re.search(r"^\s*id:\s*(\S+)", text, re.M)
    if m:
        out["id"] = m.group(1).split("#")[0].strip()
    m = re.search(r"^\s*lineage:\s*(\S+)", text, re.M)
    if m:
        out["busco_lineage_yaml"] = m.group(1).split("#")[0].strip()
    reads: list[str] = []
    for m in re.finditer(r"^\s*-\s+(\S+)", text, re.M):
        line = m.group(1).strip()
        if any(
            ext in line.lower()
            for ext in (".fastq", ".fq", ".bam", ".cram", ".fa", ".fasta", ".gz")
        ):
            reads.append(line)
    if reads:
        out["yaml_paths"] = "; ".join(reads[:6])
        if len(reads) > 6:
            out["yaml_paths"] += f"; … (+{len(reads) - 6} more)"
    return out


def hifiasm_version(log_path: Path) -> str:
    if not log_path.is_file():
        return "—"
    try:
        txt = log_path.read_text(errors="replace")[-8000:]
    except OSError:
        return "—"
    m = re.search(r"Version:\s*(\S+)", txt)
    return m.group(1) if m else "—"


def busco_lineage_from_summary(p: Path) -> str:
    if not p.is_file():
        return "—"
    try:
        for line in p.read_text(errors="replace").splitlines()[:8]:
            if "lineage dataset" in line.lower() or "The lineage dataset" in line:
                m = re.search(r"is:\s*(\S+)", line)
                if m:
                    return m.group(1)
    except OSError:
        pass
    return "—"


def plot_hist_ok(sp_dir: Path) -> tuple[bool, str]:
    png = sp_dir / "results/purge_dups/plot_hist.png"
    logp = sp_dir / "logs/purge_dups/plot_hist.log"
    if png.is_file() and png.stat().st_size > 0:
        return True, str(png)
    if logp.is_file():
        try:
            body = logp.read_text(errors="replace").strip()
            if "command not found" in body or "error" in body.lower():
                return False, body[:120]
        except OSError:
            pass
    return False, "no plot_hist.png" if not png.exists() else "empty PNG"


def species_dirs() -> list[Path]:
    dirs = []
    for p in sorted(ASSEMBLY_ROOT.iterdir()):
        if not p.is_dir():
            continue
        name = p.name
        if name in ("files",) or name.startswith("."):
            continue
        if name.startswith("Dur"):
            dirs.append(p)
    return dirs


def inventory_species(sp: Path) -> dict:
    r: dict = {"id": sp.name, "paths": []}

    def add_row(cat: str, desc: str, p: Path | None, note: str = ""):
        if p is None:
            r["paths"].append((cat, desc, None, note))
            return
        sz, mt = stat_line(p)
        r["paths"].append((cat, desc, p, note, sz, mt))

    inp = sp / "input.yaml"
    yaml_info: dict[str, str] = {}
    if inp.is_file():
        try:
            yaml_info = parse_input_yaml(inp.read_text(errors="replace"))
        except OSError:
            yaml_info = {}

    p_ctg = sp / "results/assembly/asm.bp.hic.p_ctg.fa"
    a_ctg_gfa = sp / "results/assembly/asm.bp.hic.a_ctg.gfa"
    scaff = sp / "results/scaffolding/assembly_scaffolds_final.fa"
    scaff_agp = sp / "results/scaffolding/assembly_scaffolds_final.agp"
    purged = sp / "results/purge_dups/assembly.purged.fasta"
    hap = sp / "results/purge_dups/assembly.hap.fasta"
    bed = sp / "results/purge_dups/purge_dups.bed"
    cutoffs = sp / "results/purge_dups/cutoffs"
    hifi_staged = sp / "results/pacbio/pacbio.filt.fastq.gz"

    add_row("Assembly", "Primary p_ctg FASTA (pre-YaHS)", p_ctg if p_ctg.is_file() else None)
    add_row("Assembly", "Alternate a_ctg GFA", a_ctg_gfa if a_ctg_gfa.is_file() else None)
    add_row("Assembly", "Scaffolded FASTA (YaHS)", scaff if scaff.is_file() else None)
    add_row("Assembly", "Scaffold AGP", scaff_agp if scaff_agp.is_file() else None)
    add_row("Assembly", "Purged FASTA", purged if purged.is_file() else None)
    add_row("Assembly", "Hap/dups FASTA (purge_dups)", hap if hap.is_file() else None)
    add_row("Config", "input.yaml", inp if inp.is_file() else None)

    hilog = sp / "logs/hifiasm/assembly.log"
    add_row("Logs", "hifiasm assembly.log", hilog if hilog.is_file() else None, f"version {hifiasm_version(hilog)}")

    # BUSCO: one full_table + short_summary per stage (any *_odb* lineage)
    for stage in ("initial", "purged", "scaffolded"):
        ft = find_busco_full_table(sp, stage)
        ss = find_busco_short_summary(sp, stage)
        if ft is not None:
            add_row("QC", f"BUSCO full_table ({stage})", ft)
        if ss is not None:
            add_row("QC", f"BUSCO short_summary ({stage})", ss)

    # Merqury
    for stage in ("initial", "purged", "scaffolded"):
        qv = find_one(sp / f"results/qc/merqury/{stage}", ["*.qv"])
        if qv and qv.is_file():
            add_row("QC", f"Merqury .qv ({stage})", qv)
        cs = find_one(sp / f"results/qc/merqury/{stage}", ["*.completeness.stats"])
        if cs and cs.is_file():
            add_row("QC", f"Merqury completeness ({stage})", cs)

    gs = sp / "results/pre_assembly/genomescope/output_ploidy1/summary.txt"
    add_row("QC", "GenomeScope reads ploidy1 summary", gs if gs.is_file() else None)
    rh = sp / "results/pre_assembly/reads.histo"
    add_row("QC", "Read k-mer histo (FastK)", rh if rh.is_file() else None)

    # Scaffolding / curation
    hic = find_one(sp / "results/curation", ["*.hic"])
    add_row("Scaffold", "Juicer/JBAT .hic", hic)
    jbat_agp = sp / "results/curation/out_JBAT.liftover.agp"
    add_row("Scaffold", "JBAT liftover.agp", jbat_agp if jbat_agp.is_file() else None)

    yahs_bin = sp / "results/scaffolding/assembly.bin"
    add_row("Scaffold", "YaHS assembly.bin", yahs_bin if yahs_bin.is_file() else None)
    hic_bam = sp / "results/scaffolding/mapped.PT.bam"
    add_row("Scaffold", "Hi-C mapped.PT.bam", hic_bam if hic_bam.is_file() else None)

    add_row("Purge", "purge_dups.bed", bed if bed.is_file() else None)
    add_row("Purge", "cutoffs", cutoffs if cutoffs.is_file() else None)
    add_row("Reads", "HiFi staged filt.fastq.gz", hifi_staged if hifi_staged.is_file() else None)

    # Optional / often missing
    quast = find_one(sp / "results", ["**/quast/**/report.txt"])
    if quast:
        add_row("QC", "QUAST report.txt", quast)
    seqkit = find_one(sp, ["**/seqkit*.txt", "**/*seqkit*stats*"])
    if seqkit:
        add_row("QC", "seqkit stats (glob hit)", seqkit)
    rag = find_one(sp / "results", ["**/ragtag.scaffold.fasta", "**/ragtag*.agp"])
    if rag:
        add_row("Scaffold", "RagTag output", rag)
    cool = find_one(sp / "results", ["**/*.cool", "**/*.mcool"])
    if cool:
        add_row("Scaffold", "Cool contact map", cool)
    pretext = find_one(sp / "results", ["**/*.pretext"])
    if pretext:
        add_row("Scaffold", "Pretext map", pretext)

    # Flags
    flags: list[str] = []
    if not inp.is_file():
        flags.append("missing input.yaml")
    if not p_ctg.is_file():
        flags.append("missing asm.bp.hic.p_ctg.fa")
    if not scaff.is_file():
        flags.append("missing assembly_scaffolds_final.fa")

    ok_png, ph_note = plot_hist_ok(sp)
    r["plot_hist_ok"] = ok_png
    r["plot_hist_note"] = ph_note
    if not ok_png:
        flags.append(f"purge_dups histogram: {ph_note}")

    busco_ss = find_busco_short_summary(sp, "scaffolded")
    if busco_ss is None:
        busco_ss = sp / "results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt"
    bl_run = busco_lineage_from_summary(busco_ss) if busco_ss and busco_ss.is_file() else "—"
    bl_yaml = yaml_info.get("busco_lineage_yaml", "—")
    r["busco_lineage_run"] = bl_run
    r["busco_lineage_yaml"] = bl_yaml
    if bl_yaml != "—" and bl_run != "—" and bl_yaml not in bl_run and bl_run not in bl_yaml:
        flags.append(f"BUSCO lineage yaml ({bl_yaml}) vs run ({bl_run})")

    if inp.is_file():
        for token in yaml_info.get("yaml_paths", "").split(";"):
            token = token.strip()
            if token.startswith("/") and not Path(token).exists():
                flags.append(f"missing path from yaml: {token}")

    zbs = []
    for rel in ("logs/curation/juicer.log",):
        zp = sp / rel
        if zp.is_file() and zp.stat().st_size == 0:
            zbs.append(rel)
    if zbs:
        flags.append(f"zero-byte: {', '.join(zbs)}")

    r["flags"] = flags
    r["yaml_info"] = yaml_info
    r["hifiasm_ver"] = hifiasm_version(hilog)
    return r


def md_escape_cell(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def main() -> None:
    species = species_dirs()

    chunks: list[str] = []
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    chunks.append(f"# Assembly QC file inventory (pan-Durio)\n\n")
    chunks.append(f"Auto-generated: **{now}**. Root: `{ASSEMBLY_ROOT}`.\n\n")
    chunks.append(
        "This inventory lists files used to **perform or verify** assembly QC. "
        "Per-species tables are condensed to tracked artefacts; "
        "deep BUSCO auxiliary directories are omitted.\n\n"
    )

    inv = [inventory_species(sp) for sp in species]

    chunks.append("## Summary (all species)\n\n")
    chunks.append(
        "| Species | input.yaml | Primary p_ctg.fa | Scaffold final.fa | BUSCO (run lineage) | Merqury | QUAST | seqkit | plot_hist.png | Flags |\n"
    )
    chunks.append("|---------|:------------:|:----------------:|:-------------------:|----------------------|---------|-------|--------|:-------------:|-------|\n")

    for r in inv:
        sp = ASSEMBLY_ROOT / r["id"]
        has_yaml = (sp / "input.yaml").is_file()
        p_ctg = (sp / "results/assembly/asm.bp.hic.p_ctg.fa").is_file()
        scaff = (sp / "results/scaffolding/assembly_scaffolds_final.fa").is_file()
        merq = (sp / "results/qc/merqury/scaffolded").is_dir() and any(
            (sp / "results/qc/merqury/scaffolded").glob("*.qv")
        )
        quast = bool(find_one(sp / "results", ["**/quast/**/report.txt"]))
        seqkit = bool(find_one(sp, ["**/seqkit*.txt", "**/*seqkit*stats*"]))
        flags_s = "; ".join(r["flags"]) if r["flags"] else "—"
        chunks.append(
            f"| {r['id']} | {'yes' if has_yaml else 'no'} | {'yes' if p_ctg else 'no'} | "
            f"{'yes' if scaff else 'no'} | {r['busco_lineage_run']} | "
            f"{'yes' if merq else 'no'} | {'yes' if quast else 'no'} | {'yes' if seqkit else 'no'} | "
            f"{'yes' if r['plot_hist_ok'] else 'no'} | {md_escape_cell(flags_s)} |\n"
        )

    chunks.append("\n---\n")

    for r in inv:
        sp = ASSEMBLY_ROOT / r["id"]
        chunks.append(f"\n## {r['id']}\n\n")
        yi = r.get("yaml_info") or {}
        if yi:
            chunks.append(f"- **input.yaml metadata**: `id` → `{yi.get('id', '—')}`; ")
            chunks.append(f"declared BUSCO lineage → `{yi.get('busco_lineage_yaml', '—')}`.\n")
            if yi.get("yaml_paths"):
                chunks.append(f"- **Paths referenced in yaml (subset)**: {yi['yaml_paths']}\n")
        chunks.append(f"- **hifiasm (log)**: `{r['hifiasm_ver']}`\n")
        if r["flags"]:
            chunks.append("- **Red flags / notes**:\n")
            for f in r["flags"]:
                chunks.append(f"  - {f}\n")
        else:
            chunks.append("- **Red flags / notes**: none flagged by scanner.\n")

        chunks.append("\n| Category | Description | Absolute path | Size | Modified | Notes |\n")
        chunks.append("|----------|-------------|---------------|------|----------|-------|\n")
        for row in r["paths"]:
            if len(row) == 4:
                cat, desc, p, note = row
                if p is None:
                    chunks.append(
                        f"| {cat} | {md_escape_cell(desc)} | — | — | — | {md_escape_cell(note)} |\n"
                    )
                continue
            cat, desc, p, note, sz, mt = row
            if p is None:
                chunks.append(
                    f"| {cat} | {md_escape_cell(desc)} | — | — | — | {md_escape_cell(note)} |\n"
                )
            else:
                pp = str(p)
                chunks.append(
                    f"| {cat} | {md_escape_cell(desc)} | `{pp}` | {sz} | {mt} | {md_escape_cell(note)} |\n"
                )

        missing = []
        if not (sp / "results/qc/busco/scaffolded").is_dir():
            missing.append("BUSCO scaffolded dir")
        if not find_one(sp / "results", ["**/quast/**/report.txt"]):
            missing.append("QUAST")
        if not find_one(sp, ["**/seqkit*.txt"]):
            missing.append("seqkit stats output")
        if not r["plot_hist_ok"]:
            missing.append("purge_dups plot_hist.png")
        if not find_one(sp / "results", ["**/ragtag.scaffold.fasta"]):
            missing.append("RagTag (not found)")
        if not find_one(sp / "results", ["**/*.cool", "**/*.mcool"]):
            missing.append(".cool/.mcool (not found)")
        if not find_one(sp / "results", ["**/*.pretext"]):
            missing.append(".pretext (not found)")
        chunks.append(
            f"\n**Likely missing (for pan-project parity)** — {', '.join(missing)}.\n"
        )

    chunks.append("\n---\n\n## Global sample sheet\n\n")
    ss = Path("/home/proj_202504p2_BD-MED/abner/durio/samplesheet_hic.csv")
    if ss.is_file():
        sz, mt = stat_line(ss)
        chunks.append(f"- `{ss}` — {sz}, modified {mt}\n")
    else:
        chunks.append("- `samplesheet_hic.csv` not found at project root.\n")

    chunks.append("\n---\n\n## Regenerating this inventory\n\n")
    chunks.append(
        "From the `durio` repository root:\n\n"
        "```bash\n"
        "python3 assembly/scripts/generate_qc_inventory.py\n"
        "```\n\n"
        "The script only scans directories under `assembly/` whose names start with `Dur` "
        "(twelve species in this snapshot).\n"
    )

    OUT_PATH.write_text("".join(chunks), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({len(species)} species)")


if __name__ == "__main__":
    main()
