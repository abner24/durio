"""Cluster paths for Durio comparative jobs.

These PBS scripts are meant to run on the HPC checkout
(/home/proj_202504p2_BD-MED/abner/durio), where OrthoFinder, BRAKER,
proteomes, and the existing MCMCtree Hessian live. Override with env CMP/ROOT.
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(os.environ.get("DURIO_ROOT", "/home/proj_202504p2_BD-MED/abner/durio"))
CMP = Path(os.environ.get("CMP", str(ROOT / "comparison")))
ENV = Path(
    os.environ.get(
        "DURIO_ENV",
        "/home/chroma.phytos.nmslms/miniforge3/envs/durio_evol",
    )
)
OF = CMP / "02_orthofinder" / "round3_all13_plus_cacao_OF3" / "Results_Aug06"
MSA_DIR = OF / "MultipleSequenceAlignments"
PROTEOMES = CMP / "01_proteomes"
MCMC_DIR = CMP / "12_mcmctree"
PUBLIC_DIR = CMP / "13_public_assemblies"
JCVI_DIR = CMP / "15_jcvi"

OUTGROUP = "Theobroma_cacao"
HERRANIA = "Herrania_umbratica"
HYBRIDS = frozenset({"DurMK", "DurSul"})

MCMC_TAXA = (
    OUTGROUP,
    "DurSin",
    "DurTes",
    "DurBru",
    "DurOxl",
    "DurDul",
    "DurKut",
    "DurGra_Og",
    "T2T_MK_mat",
)
MCMC_TAXA_HERRANIA = (HERRANIA,) + MCMC_TAXA

ROOT_LOWER_100MA = 0.60
ROOT_UPPER_100MA = 0.90
# Theobroma–Herrania (Byttnerioideae) secondary bound, 5–20 Ma.
CACAO_HERRANIA_LOWER = 0.05
CACAO_HERRANIA_UPPER = 0.20

HERRANIA_PROTEIN_URL = (
    "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/168/275/"
    "GCF_002168275.1_ASM216827v2/"
    "GCF_002168275.1_ASM216827v2_protein.faa.gz"
)

T2T_GENOME = Path(
    "/home/proj_202504p2_BD-MED/brendan/projects/t2t/annotations/data/"
    "mk.t2t.mat.chr.fasta"
)
T2T_GTF = Path(
    "/home/proj_202504p2_BD-MED/brendan/projects/t2t/annotations/"
    "post_process_t2t_mat/complete_genes.gtf"
)

GENOME_FASTA = {
    "DurBru": ROOT / "assembly/DurBru/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurDatoAli": ROOT / "assembly/DurDatoAli/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurDul": ROOT / "assembly/DurDul/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurGra_Og": ROOT / "assembly/DurGra_Og/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurGra_Simpur": ROOT / "assembly/DurGra_Simpur/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurKut": ROOT / "assembly/DurKut/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurMK": ROOT / "assembly/DurMK/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurOxl": ROOT / "assembly/DurOxl/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurSin": ROOT / "assembly/DurSin/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurSul": ROOT / "assembly/DurSul/results/curation/samba_gapfill/out_JBAT.FINAL.samba.sorted.fa",
    "DurTes": ROOT / "annotation/DurTes/genome.filtered_min1Mb.fa",
    "DurZibPV": ROOT / "assembly/DurZibPV/results/scaffolding/assembly_scaffolds_final.fa",
    "T2T_MK_mat": T2T_GENOME,
}

GTF_CANDIDATES = {
    "T2T_MK_mat": [T2T_GTF],
}


def gtf_paths(sample: str) -> list[Path]:
    if sample in GTF_CANDIDATES:
        return list(GTF_CANDIDATES[sample])
    return [
        ROOT / f"annotation/{sample}/output/{sample}/results/braker.gtf",
        ROOT / f"annotation_red/{sample}/output/{sample}/results/braker.gtf",
        ROOT / f"annotation/{sample}/results/braker.gtf",
    ]


def proteome_faa(sample: str) -> Path:
    return PROTEOMES / f"{sample}.faa"


JCVI_PAIRS = (
    ("T2T_MK_mat", "DurZibPV"),
    ("T2T_MK_mat", "DurDatoAli"),
    ("T2T_MK_mat", "DurGra_Og"),
    ("T2T_MK_mat", "DurSin"),
    ("T2T_MK_mat", "DurTes"),
    ("T2T_MK_mat", "DurOxl"),
    ("DurGra_Og", "DurMK"),
    ("T2T_MK_mat", "DurSul"),
)

KARYOTYPE_TRACKS = ("T2T_MK_mat", "DurZibPV", "DurDatoAli", "DurGra_Og")
