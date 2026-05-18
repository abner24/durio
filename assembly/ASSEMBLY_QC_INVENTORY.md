# Assembly QC file inventory (pan-Durio)

Auto-generated: **2026-05-13 15:51**. Root: `/home/proj_202504p2_BD-MED/abner/durio/assembly`.

This inventory lists files used to **perform or verify** assembly QC. Per-species tables are condensed to tracked artefacts; deep BUSCO auxiliary directories are omitted.

## Summary (all species)

| Species | input.yaml | Primary p_ctg.fa | Scaffold final.fa | BUSCO (run lineage) | Merqury | QUAST | seqkit | plot_hist.png | Flags |
|---------|:------------:|:----------------:|:-------------------:|----------------------|---------|-------|--------|:-------------:|-------|
| DurBru | no | yes | yes | embryophyta_odb10 | yes | no | no | no | missing input.yaml; purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; zero-byte: logs/curation/juicer.log |
| DurDatoAli | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurDatoA.cram; zero-byte: logs/curation/juicer.log |
| DurDul | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurDul.cram; zero-byte: logs/curation/juicer.log |
| DurGra_Og | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurGra_Og.cram; zero-byte: logs/curation/juicer.log |
| DurGra_Simpur | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurSim.cram; zero-byte: logs/curation/juicer.log |
| DurKut | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurKut.cram; zero-byte: logs/curation/juicer.log |
| DurMK | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/Dmk_Omc.cram; zero-byte: logs/curation/juicer.log |
| DurOxl | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurOxy.cram; zero-byte: logs/curation/juicer.log |
| DurSin | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/Dsin_Omc.cram; zero-byte: logs/curation/juicer.log |
| DurSul | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurSul_k.cram; zero-byte: logs/curation/juicer.log |
| DurTes | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DT_OmniC.cram; zero-byte: logs/curation/juicer.log |
| DurZibPV | yes | yes | yes | embryophyta_odb10 | yes | no | no | no | purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found; BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10); missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurPV.cram; zero-byte: logs/curation/juicer.log |

---

## DurBru

- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - missing input.yaml
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/assembly/asm.bp.hic.p_ctg.fa` | 801.29 MiB | 2026-04-06 21:34 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/assembly/asm.bp.hic.a_ctg.gfa` | 817.21 MiB | 2026-04-06 21:08 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/scaffolding/assembly_scaffolds_final.fa` | 779.86 MiB | 2026-04-07 04:37 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/scaffolding/assembly_scaffolds_final.agp` | 56.14 KiB | 2026-04-07 04:37 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/purge_dups/assembly.purged.fasta` | 767.05 MiB | 2026-04-06 23:03 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/purge_dups/assembly.hap.fasta` | 24.35 MiB | 2026-04-06 23:03 |  |
| Config | input.yaml | — | — | — |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/logs/hifiasm/assembly.log` | 53.09 KiB | 2026-04-06 21:33 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 277.60 KiB | 2026-04-06 21:48 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 977 B | 2026-04-06 21:48 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 278.91 KiB | 2026-04-07 04:51 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 988 B | 2026-04-07 04:51 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 17.72 KiB | 2026-04-07 10:58 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-07 10:59 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/merqury/purged/purged.assembly.purged.qv` | 12.17 KiB | 2026-04-07 10:58 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-07 10:59 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 13.90 KiB | 2026-04-07 10:58 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-07 10:59 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-06 17:29 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/pre_assembly/reads.histo` | 9.46 KiB | 2026-04-06 17:28 |  |
| Scaffold | Juicer/JBAT .hic | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/curation/out_JBAT.hic` | 167.23 MiB | 2026-04-07 04:47 |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/curation/out_JBAT.liftover.agp` | 44.46 KiB | 2026-04-07 04:38 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/scaffolding/assembly.bin` | 342.39 MiB | 2026-04-07 04:37 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/scaffolding/mapped.PT.bam` | 3.91 GiB | 2026-04-07 04:35 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/purge_dups/purge_dups.bed` | 10.35 KiB | 2026-04-06 23:03 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/purge_dups/cutoffs` | 18 B | 2026-04-06 23:02 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurBru/results/pacbio/pacbio.filt.fastq.gz` | 27.03 GiB | 2026-04-06 17:07 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurDatoAli

- **input.yaml metadata**: `id` → `DurDatoAli`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_Dat_Ak.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurDatoA.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurDatoA.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/assembly/asm.bp.hic.p_ctg.fa` | 863.27 MiB | 2026-04-07 21:55 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/assembly/asm.bp.hic.a_ctg.gfa` | 902.76 MiB | 2026-04-07 21:31 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/scaffolding/assembly_scaffolds_final.fa` | 813.80 MiB | 2026-04-08 03:52 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/scaffolding/assembly_scaffolds_final.agp` | 74.34 KiB | 2026-04-08 03:52 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/purge_dups/assembly.purged.fasta` | 800.43 MiB | 2026-04-07 23:16 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/purge_dups/assembly.hap.fasta` | 52.19 MiB | 2026-04-07 23:16 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/input.yaml` | 1.17 KiB | 2026-02-04 11:29 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/logs/hifiasm/assembly.log` | 41.72 KiB | 2026-04-07 21:55 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 275.19 KiB | 2026-04-07 22:13 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 984 B | 2026-04-07 22:13 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 276.34 KiB | 2026-04-08 04:06 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 994 B | 2026-04-08 04:06 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 27.03 KiB | 2026-04-07 22:00 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-07 22:02 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/merqury/purged/purged.assembly.purged.qv` | 14.59 KiB | 2026-04-07 23:21 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-07 23:23 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 14.43 KiB | 2026-04-08 03:56 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 03:58 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 18:18 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/pre_assembly/reads.histo` | 9.44 KiB | 2026-04-07 18:18 |  |
| Scaffold | Juicer/JBAT .hic | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/curation/out_JBAT.hic` | 299.73 MiB | 2026-04-08 04:10 |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/curation/out_JBAT.liftover.agp` | 52.87 KiB | 2026-04-08 03:52 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/scaffolding/assembly.bin` | 777.97 MiB | 2026-04-08 03:52 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/scaffolding/mapped.PT.bam` | 8.72 GiB | 2026-04-08 03:48 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/purge_dups/purge_dups.bed` | 19.85 KiB | 2026-04-07 23:16 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/purge_dups/cutoffs` | 18 B | 2026-04-07 23:15 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDatoAli/results/pacbio/pacbio.filt.fastq.gz` | 24.64 GiB | 2026-04-07 17:57 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurDul

- **input.yaml metadata**: `id` → `DurDul`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/DurDul.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurDul.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurDul.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/assembly/asm.bp.hic.p_ctg.fa` | 747.64 MiB | 2026-04-08 01:15 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/assembly/asm.bp.hic.a_ctg.gfa` | 804.33 MiB | 2026-04-08 00:47 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/scaffolding/assembly_scaffolds_final.fa` | 719.92 MiB | 2026-04-08 11:15 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/scaffolding/assembly_scaffolds_final.agp` | 19.12 KiB | 2026-04-08 11:15 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/purge_dups/assembly.purged.fasta` | 708.12 MiB | 2026-04-08 03:08 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/purge_dups/assembly.hap.fasta` | 30.30 MiB | 2026-04-08 03:08 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/input.yaml` | 1.14 KiB | 2026-02-04 23:03 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/logs/hifiasm/assembly.log` | 69.88 KiB | 2026-04-08 01:15 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 276.95 KiB | 2026-04-08 01:30 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 977 B | 2026-04-08 01:30 |  |
| QC | BUSCO full_table (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/busco/purged/run_embryophyta_odb10/full_table.tsv` | 280.97 KiB | 2026-04-08 03:21 |  |
| QC | BUSCO short_summary (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/busco/purged/short_summary.specific.embryophyta_odb10.purged.txt` | 981 B | 2026-04-08 03:21 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 278.17 KiB | 2026-04-08 11:28 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 988 B | 2026-04-08 11:28 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 11.59 KiB | 2026-04-08 01:20 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 01:22 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/merqury/purged/purged.assembly.purged.qv` | 5.12 KiB | 2026-04-08 03:12 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 03:14 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 6.23 KiB | 2026-04-08 11:19 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 11:21 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 18:46 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/pre_assembly/reads.histo` | 9.60 KiB | 2026-04-07 18:45 |  |
| Scaffold | Juicer/JBAT .hic | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/curation/out_JBAT.hic` | 622.40 MiB | 2026-04-08 11:35 |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/curation/out_JBAT.liftover.agp` | 17.35 KiB | 2026-04-08 11:16 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/scaffolding/assembly.bin` | 1.20 GiB | 2026-04-08 11:15 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/scaffolding/mapped.PT.bam` | 19.52 GiB | 2026-04-08 11:07 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/purge_dups/purge_dups.bed` | 11.95 KiB | 2026-04-08 03:08 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/purge_dups/cutoffs` | 19 B | 2026-04-08 03:07 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurDul/results/pacbio/pacbio.filt.fastq.gz` | 34.32 GiB | 2026-04-07 18:18 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurGra_Og

- **input.yaml metadata**: `id` → `DurGra_Og`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_org_PB.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurGra_Og.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurGra_Og.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/assembly/asm.bp.hic.p_ctg.fa` | 1.47 GiB | 2026-04-07 19:57 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/assembly/asm.bp.hic.a_ctg.gfa` | 224.94 MiB | 2026-04-07 19:08 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/scaffolding/assembly_scaffolds_final.fa` | 1.15 GiB | 2026-04-08 07:46 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/scaffolding/assembly_scaffolds_final.agp` | 42.72 KiB | 2026-04-08 07:46 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/purge_dups/assembly.purged.fasta` | 1.13 GiB | 2026-04-07 21:10 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/purge_dups/assembly.hap.fasta` | 322.50 MiB | 2026-04-07 21:10 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/input.yaml` | 1.15 KiB | 2026-02-05 09:53 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/logs/hifiasm/assembly.log` | 30.56 KiB | 2026-04-07 19:56 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 546.99 KiB | 2026-04-07 20:24 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 981 B | 2026-04-07 20:24 |  |
| QC | BUSCO full_table (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/busco/purged/run_embryophyta_odb10/full_table.tsv` | 460.30 KiB | 2026-04-07 21:34 |  |
| QC | BUSCO short_summary (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/busco/purged/short_summary.specific.embryophyta_odb10.purged.txt` | 985 B | 2026-04-07 21:35 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 457.50 KiB | 2026-04-08 08:06 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 991 B | 2026-04-08 08:06 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 24.96 KiB | 2026-04-07 20:03 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-07 20:04 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/merqury/purged/purged.assembly.purged.qv` | 8.86 KiB | 2026-04-07 21:14 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-07 21:15 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 8.11 KiB | 2026-04-08 07:51 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 07:52 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 17:58 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/pre_assembly/reads.histo` | 9.07 KiB | 2026-04-07 17:57 |  |
| Scaffold | Juicer/JBAT .hic | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/curation/out_JBAT.hic` | 495.79 MiB | 2026-04-08 08:04 |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/curation/out_JBAT.liftover.agp` | 29.76 KiB | 2026-04-08 07:47 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/scaffolding/assembly.bin` | 1017.48 MiB | 2026-04-08 07:46 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/scaffolding/mapped.PT.bam` | 13.09 GiB | 2026-04-08 07:40 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/purge_dups/purge_dups.bed` | 28.14 KiB | 2026-04-07 21:10 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/purge_dups/cutoffs` | 16 B | 2026-04-07 21:08 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Og/results/pacbio/pacbio.filt.fastq.gz` | 19.28 GiB | 2026-04-07 17:44 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurGra_Simpur

- **input.yaml metadata**: `id` → `DurGra_Sim`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_simpur.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurSim.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurSim.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/assembly/asm.bp.hic.p_ctg.fa` | 856.13 MiB | 2026-04-08 02:21 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/assembly/asm.bp.hic.a_ctg.gfa` | 894.35 MiB | 2026-04-08 01:41 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/scaffolding/assembly_scaffolds_final.fa` | 730.21 MiB | 2026-04-08 12:10 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/scaffolding/assembly_scaffolds_final.agp` | 17.34 KiB | 2026-04-08 12:10 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/purge_dups/assembly.purged.fasta` | 718.24 MiB | 2026-04-08 03:26 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/purge_dups/assembly.hap.fasta` | 127.32 MiB | 2026-04-08 03:26 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/input.yaml` | 1.15 KiB | 2026-02-04 10:53 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/logs/hifiasm/assembly.log` | 37.54 KiB | 2026-04-08 02:21 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 277.88 KiB | 2026-04-08 02:36 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 985 B | 2026-04-08 02:36 |  |
| QC | BUSCO full_table (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/busco/purged/run_embryophyta_odb10/full_table.tsv` | 282.68 KiB | 2026-04-08 03:39 |  |
| QC | BUSCO short_summary (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/busco/purged/short_summary.specific.embryophyta_odb10.purged.txt` | 989 B | 2026-04-08 03:39 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 280.32 KiB | 2026-04-08 12:22 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 996 B | 2026-04-08 12:22 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 11.79 KiB | 2026-04-08 02:25 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 02:26 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/merqury/purged/purged.assembly.purged.qv` | 5.04 KiB | 2026-04-08 03:30 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 03:31 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 4.76 KiB | 2026-04-08 12:14 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 12:15 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 23:47 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/pre_assembly/reads.histo` | 9.28 KiB | 2026-04-07 23:47 |  |
| Scaffold | Juicer/JBAT .hic | — | — | — |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/curation/out_JBAT.liftover.agp` | 14.01 KiB | 2026-04-08 12:10 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/scaffolding/assembly.bin` | 1.64 GiB | 2026-04-08 12:10 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/scaffolding/mapped.PT.bam` | 22.38 GiB | 2026-04-08 12:00 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/purge_dups/purge_dups.bed` | 11.90 KiB | 2026-04-08 03:26 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/purge_dups/cutoffs` | 18 B | 2026-04-08 03:25 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurGra_Simpur/results/pacbio/pacbio.filt.fastq.gz` | 25.84 GiB | 2026-04-07 23:32 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurKut

- **input.yaml metadata**: `id` → `DurKut`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_pulaPB.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurKut.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurKut.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/assembly/asm.bp.hic.p_ctg.fa` | 914.55 MiB | 2026-04-08 02:37 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/assembly/asm.bp.hic.a_ctg.gfa` | 871.19 MiB | 2026-04-08 01:58 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/scaffolding/assembly_scaffolds_final.fa` | 794.43 MiB | 2026-04-08 14:04 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/scaffolding/assembly_scaffolds_final.agp` | 39.34 KiB | 2026-04-08 14:04 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/purge_dups/assembly.purged.fasta` | 781.41 MiB | 2026-04-08 03:47 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/purge_dups/assembly.hap.fasta` | 121.86 MiB | 2026-04-08 03:47 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/input.yaml` | 1.15 KiB | 2026-02-05 09:52 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/logs/hifiasm/assembly.log` | 48.73 KiB | 2026-04-08 02:37 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 278.68 KiB | 2026-04-08 02:54 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 979 B | 2026-04-08 02:54 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 279.89 KiB | 2026-04-08 14:19 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 988 B | 2026-04-08 14:19 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 28.38 KiB | 2026-04-08 02:41 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 02:43 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/merqury/purged/purged.assembly.purged.qv` | 14.25 KiB | 2026-04-08 03:51 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 03:52 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 14.73 KiB | 2026-04-08 14:08 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 14:09 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 23:48 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/pre_assembly/reads.histo` | 9.23 KiB | 2026-04-07 23:47 |  |
| Scaffold | Juicer/JBAT .hic | — | — | — |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/curation/out_JBAT.liftover.agp` | 37.88 KiB | 2026-04-08 14:05 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/scaffolding/assembly.bin` | 2.57 GiB | 2026-04-08 14:04 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/scaffolding/mapped.PT.bam` | 33.63 GiB | 2026-04-08 13:51 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/purge_dups/purge_dups.bed` | 24.15 KiB | 2026-04-08 03:47 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/purge_dups/cutoffs` | 17 B | 2026-04-08 03:46 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurKut/results/pacbio/pacbio.filt.fastq.gz` | 25.02 GiB | 2026-04-07 23:32 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurMK

- **input.yaml metadata**: `id` → `DurMK`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_m_k_F2.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/Dmk_Omc.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/Dmk_Omc.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/assembly/asm.bp.hic.p_ctg.fa` | 966.68 MiB | 2026-04-08 01:24 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/assembly/asm.bp.hic.a_ctg.gfa` | 849.60 MiB | 2026-04-08 00:26 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/scaffolding/assembly_scaffolds_final.fa` | 806.81 MiB | 2026-04-08 10:52 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/scaffolding/assembly_scaffolds_final.agp` | 61.74 KiB | 2026-04-08 10:52 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/purge_dups/assembly.purged.fasta` | 793.57 MiB | 2026-04-08 02:13 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/purge_dups/assembly.hap.fasta` | 161.19 MiB | 2026-04-08 02:13 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/input.yaml` | 1.17 KiB | 2026-02-03 17:44 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/logs/hifiasm/assembly.log` | 27.94 KiB | 2026-04-08 01:24 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 281.34 KiB | 2026-04-08 01:41 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 979 B | 2026-04-08 01:41 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 281.19 KiB | 2026-04-08 11:07 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 988 B | 2026-04-08 11:07 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 36.21 KiB | 2026-04-08 01:29 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 01:31 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/merqury/purged/purged.assembly.purged.qv` | 19.32 KiB | 2026-04-08 02:18 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 02:19 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 19.42 KiB | 2026-04-08 10:57 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 10:58 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 23:36 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/pre_assembly/reads.histo` | 9.09 KiB | 2026-04-07 23:36 |  |
| Scaffold | Juicer/JBAT .hic | — | — | — |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/curation/out_JBAT.liftover.agp` | 54.13 KiB | 2026-04-08 10:53 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/scaffolding/assembly.bin` | 1.94 GiB | 2026-04-08 10:52 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/scaffolding/mapped.PT.bam` | 28.55 GiB | 2026-04-08 10:41 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/purge_dups/purge_dups.bed` | 26.34 KiB | 2026-04-08 02:13 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/purge_dups/cutoffs` | 16 B | 2026-04-08 02:11 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurMK/results/pacbio/pacbio.filt.fastq.gz` | 20.52 GiB | 2026-04-07 23:23 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurOxl

- **input.yaml metadata**: `id` → `DurOxl`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_oxl_PB.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurOxy.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurOxy.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/assembly/asm.bp.hic.p_ctg.fa` | 691.11 MiB | 2026-04-08 03:04 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/assembly/asm.bp.hic.a_ctg.gfa` | 672.23 MiB | 2026-04-08 02:35 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/scaffolding/assembly_scaffolds_final.fa` | 651.70 MiB | 2026-04-08 12:00 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/scaffolding/assembly_scaffolds_final.agp` | 7.55 KiB | 2026-04-08 12:00 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/purge_dups/assembly.purged.fasta` | 641.01 MiB | 2026-04-08 04:12 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/purge_dups/assembly.hap.fasta` | 41.57 MiB | 2026-04-08 04:12 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/input.yaml` | 1.15 KiB | 2026-02-04 11:29 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/logs/hifiasm/assembly.log` | 36.41 KiB | 2026-04-08 03:03 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 277.02 KiB | 2026-04-08 03:16 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 978 B | 2026-04-08 03:16 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 277.70 KiB | 2026-04-08 12:12 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 988 B | 2026-04-08 12:12 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 6.49 KiB | 2026-04-08 03:08 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 03:09 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/merqury/purged/purged.assembly.purged.qv` | 1.83 KiB | 2026-04-08 04:16 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 04:17 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 1.86 KiB | 2026-04-08 12:04 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 12:05 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 23:50 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/pre_assembly/reads.histo` | 9.20 KiB | 2026-04-07 23:50 |  |
| Scaffold | Juicer/JBAT .hic | — | — | — |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/curation/out_JBAT.liftover.agp` | 5.90 KiB | 2026-04-08 12:01 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/scaffolding/assembly.bin` | 1.23 GiB | 2026-04-08 12:00 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/scaffolding/mapped.PT.bam` | 19.35 GiB | 2026-04-08 11:53 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/purge_dups/purge_dups.bed` | 9.03 KiB | 2026-04-08 04:12 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/purge_dups/cutoffs` | 18 B | 2026-04-08 04:11 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurOxl/results/pacbio/pacbio.filt.fastq.gz` | 24.88 GiB | 2026-04-07 23:35 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurSin

- **input.yaml metadata**: `id` → `DurSin`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_Sin_PB.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/Dsin_Omc.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/Dsin_Omc.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/assembly/asm.bp.hic.p_ctg.fa` | 819.43 MiB | 2026-04-08 04:41 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/assembly/asm.bp.hic.a_ctg.gfa` | 716.57 MiB | 2026-04-08 04:08 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/scaffolding/assembly_scaffolds_final.fa` | 752.31 MiB | 2026-04-08 13:57 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/scaffolding/assembly_scaffolds_final.agp` | 46.42 KiB | 2026-04-08 13:57 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/purge_dups/assembly.purged.fasta` | 739.97 MiB | 2026-04-08 06:02 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/purge_dups/assembly.hap.fasta` | 69.36 MiB | 2026-04-08 06:02 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/input.yaml` | 1.16 KiB | 2026-02-03 17:47 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/logs/hifiasm/assembly.log` | 43.99 KiB | 2026-04-08 04:40 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 276.76 KiB | 2026-04-08 04:56 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 979 B | 2026-04-08 04:56 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 278.24 KiB | 2026-04-08 14:11 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 988 B | 2026-04-08 14:11 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 30.84 KiB | 2026-04-08 04:45 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 04:47 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/merqury/purged/purged.assembly.purged.qv` | 15.34 KiB | 2026-04-08 06:07 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 06:08 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 16.89 KiB | 2026-04-08 14:01 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 14:03 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 23:54 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/pre_assembly/reads.histo` | 9.40 KiB | 2026-04-07 23:54 |  |
| Scaffold | Juicer/JBAT .hic | — | — | — |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/curation/out_JBAT.liftover.agp` | 44.20 KiB | 2026-04-08 13:58 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/scaffolding/assembly.bin` | 1.43 GiB | 2026-04-08 13:57 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/scaffolding/mapped.PT.bam` | 16.32 GiB | 2026-04-08 13:50 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/purge_dups/purge_dups.bed` | 22.98 KiB | 2026-04-08 06:02 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/purge_dups/cutoffs` | 18 B | 2026-04-08 06:01 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSin/results/pacbio/pacbio.filt.fastq.gz` | 22.06 GiB | 2026-04-07 23:36 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurSul

- **input.yaml metadata**: `id` → `DurSul`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_Sul_K.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurSul_k.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurSul_k.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/assembly/asm.bp.hic.p_ctg.fa` | 870.57 MiB | 2026-04-08 00:44 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/assembly/asm.bp.hic.a_ctg.gfa` | 814.55 MiB | 2026-04-08 00:19 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/scaffolding/assembly_scaffolds_final.fa` | 723.68 MiB | 2026-04-08 06:47 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/scaffolding/assembly_scaffolds_final.agp` | 57.01 KiB | 2026-04-08 06:47 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/purge_dups/assembly.purged.fasta` | 711.79 MiB | 2026-04-08 02:07 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/purge_dups/assembly.hap.fasta` | 148.03 MiB | 2026-04-08 02:07 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/input.yaml` | 1.17 KiB | 2026-02-04 11:37 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/logs/hifiasm/assembly.log` | 26.11 KiB | 2026-04-08 00:43 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 277.14 KiB | 2026-04-08 01:01 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 978 B | 2026-04-08 01:01 |  |
| QC | BUSCO full_table (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/busco/purged/run_embryophyta_odb10/full_table.tsv` | 279.39 KiB | 2026-04-08 02:20 |  |
| QC | BUSCO short_summary (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/busco/purged/short_summary.specific.embryophyta_odb10.purged.txt` | 982 B | 2026-04-08 02:20 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 275.85 KiB | 2026-04-08 07:00 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 989 B | 2026-04-08 07:00 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 13.83 KiB | 2026-04-08 00:49 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 00:51 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/merqury/purged/purged.assembly.purged.qv` | 5.48 KiB | 2026-04-08 02:12 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 02:13 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 8.83 KiB | 2026-04-08 06:51 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 06:53 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 23:33 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/pre_assembly/reads.histo` | 8.98 KiB | 2026-04-07 23:33 |  |
| Scaffold | Juicer/JBAT .hic | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/curation/out_JBAT.hic` | 179.93 MiB | 2026-04-08 07:04 |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/curation/out_JBAT.liftover.agp` | 38.15 KiB | 2026-04-08 06:48 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/scaffolding/assembly.bin` | 1.70 GiB | 2026-04-08 06:47 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/scaffolding/mapped.PT.bam` | 13.17 GiB | 2026-04-08 06:39 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/purge_dups/purge_dups.bed` | 15.37 KiB | 2026-04-08 02:07 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/purge_dups/cutoffs` | 16 B | 2026-04-08 01:33 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurSul/results/pacbio/pacbio.filt.fastq.gz` | 20.95 GiB | 2026-04-07 23:20 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurTes

- **input.yaml metadata**: `id` → `DurTes`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/DurTes.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DT_OmniC.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DT_OmniC.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/assembly/asm.bp.hic.p_ctg.fa` | 785.87 MiB | 2026-04-08 01:45 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/assembly/asm.bp.hic.a_ctg.gfa` | 680.06 MiB | 2026-04-08 01:21 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/scaffolding/assembly_scaffolds_final.fa` | 757.22 MiB | 2026-04-08 11:16 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/scaffolding/assembly_scaffolds_final.agp` | 4.22 KiB | 2026-04-08 11:16 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/purge_dups/assembly.purged.fasta` | 744.81 MiB | 2026-04-08 03:17 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/purge_dups/assembly.hap.fasta` | 31.36 MiB | 2026-04-08 03:17 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/input.yaml` | 1.15 KiB | 2026-02-04 13:23 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/logs/hifiasm/assembly.log` | 39.85 KiB | 2026-04-08 01:45 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 274.69 KiB | 2026-04-08 01:59 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 978 B | 2026-04-08 01:59 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 275.96 KiB | 2026-04-08 11:29 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 987 B | 2026-04-08 11:29 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 6.58 KiB | 2026-04-08 01:50 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 01:51 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/merqury/purged/purged.assembly.purged.qv` | 1.44 KiB | 2026-04-08 03:21 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 03:22 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 1.79 KiB | 2026-04-08 11:20 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 11:22 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-07 23:42 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/pre_assembly/reads.histo` | 9.23 KiB | 2026-04-07 23:42 |  |
| Scaffold | Juicer/JBAT .hic | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/curation/out_JBAT.hic` | 153.63 MiB | 2026-04-08 11:24 |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/curation/out_JBAT.liftover.agp` | 4.40 KiB | 2026-04-08 11:17 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/scaffolding/assembly.bin` | 81.17 MiB | 2026-04-08 11:16 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/scaffolding/mapped.PT.bam` | 2.46 GiB | 2026-04-08 11:15 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/purge_dups/purge_dups.bed` | 9.74 KiB | 2026-04-08 03:16 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/purge_dups/cutoffs` | 17 B | 2026-04-08 03:15 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurTes/results/pacbio/pacbio.filt.fastq.gz` | 27.60 GiB | 2026-04-07 23:27 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

## DurZibPV

- **input.yaml metadata**: `id` → `DurZibPV`; declared BUSCO lineage → `viridiplantae_odb12`.
- **Paths referenced in yaml (subset)**: /home/proj_202504p2_BD-MED/abner/durio/raw_data/PBTK_BAM2FASTQ/D_Put_Vn.fastq.gz; /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurPV.cram
- **hifiasm (log)**: `0.25.0-r726`
- **Red flags / notes**:
  - purge_dups histogram: /bin/bash: line 2: hist_plot.py: command not found
  - BUSCO lineage yaml (viridiplantae_odb12) vs run (embryophyta_odb10)
  - missing path from yaml: /home/proj_202504p2_BD-MED/abner/durio/raw_data/cram/DurPV.cram
  - zero-byte: logs/curation/juicer.log

| Category | Description | Absolute path | Size | Modified | Notes |
|----------|-------------|---------------|------|----------|-------|
| Assembly | Primary p_ctg FASTA (pre-YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/assembly/asm.bp.hic.p_ctg.fa` | 807.28 MiB | 2026-04-08 06:06 |  |
| Assembly | Alternate a_ctg GFA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/assembly/asm.bp.hic.a_ctg.gfa` | 859.96 MiB | 2026-04-08 05:38 |  |
| Assembly | Scaffolded FASTA (YaHS) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/scaffolding/assembly_scaffolds_final.fa` | 758.62 MiB | 2026-04-08 13:49 |  |
| Assembly | Scaffold AGP | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/scaffolding/assembly_scaffolds_final.agp` | 72.54 KiB | 2026-04-08 13:49 |  |
| Assembly | Purged FASTA | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/purge_dups/assembly.purged.fasta` | 746.16 MiB | 2026-04-08 07:50 |  |
| Assembly | Hap/dups FASTA (purge_dups) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/purge_dups/assembly.hap.fasta` | 51.16 MiB | 2026-04-08 07:50 |  |
| Config | input.yaml | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/input.yaml` | 1.17 KiB | 2026-02-04 11:34 |  |
| Logs | hifiasm assembly.log | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/logs/hifiasm/assembly.log` | 44.44 KiB | 2026-04-08 06:06 | version 0.25.0-r726 |
| QC | BUSCO full_table (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/busco/initial/run_embryophyta_odb10/full_table.tsv` | 273.72 KiB | 2026-04-08 06:21 |  |
| QC | BUSCO short_summary (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/busco/initial/short_summary.specific.embryophyta_odb10.initial.txt` | 981 B | 2026-04-08 06:21 |  |
| QC | BUSCO full_table (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/busco/scaffolded/run_embryophyta_odb10/full_table.tsv` | 273.17 KiB | 2026-04-08 14:03 |  |
| QC | BUSCO short_summary (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/busco/scaffolded/short_summary.specific.embryophyta_odb10.scaffolded.txt` | 994 B | 2026-04-08 14:03 |  |
| QC | Merqury .qv (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/merqury/initial/initial.asm.bp.hic.p_ctg.qv` | 14.76 KiB | 2026-04-08 06:11 |  |
| QC | Merqury completeness (initial) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/merqury/initial/initial.completeness.stats` | 95 B | 2026-04-08 06:13 |  |
| QC | Merqury .qv (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/merqury/purged/purged.assembly.purged.qv` | 6.84 KiB | 2026-04-08 07:55 |  |
| QC | Merqury completeness (purged) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/merqury/purged/purged.completeness.stats` | 94 B | 2026-04-08 07:57 |  |
| QC | Merqury .qv (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/merqury/scaffolded/scaffolded.assembly_scaffolds_final.qv` | 22.12 KiB | 2026-04-08 13:54 |  |
| QC | Merqury completeness (scaffolded) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/qc/merqury/scaffolded/scaffolded.completeness.stats` | 103 B | 2026-04-08 13:56 |  |
| QC | GenomeScope reads ploidy1 summary | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/pre_assembly/genomescope/output_ploidy1/summary.txt` | 620 B | 2026-04-08 00:18 |  |
| QC | Read k-mer histo (FastK) | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/pre_assembly/reads.histo` | 9.55 KiB | 2026-04-08 00:18 |  |
| Scaffold | Juicer/JBAT .hic | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/curation/out_JBAT.hic` | 167.16 MiB | 2026-04-08 14:07 |  |
| Scaffold | JBAT liftover.agp | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/curation/out_JBAT.liftover.agp` | 66.45 KiB | 2026-04-08 13:50 |  |
| Scaffold | YaHS assembly.bin | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/scaffolding/assembly.bin` | 2.49 GiB | 2026-04-08 13:49 |  |
| Scaffold | Hi-C mapped.PT.bam | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/scaffolding/mapped.PT.bam` | 18.17 GiB | 2026-04-08 13:37 |  |
| Purge | purge_dups.bed | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/purge_dups/purge_dups.bed` | 14.55 KiB | 2026-04-08 07:50 |  |
| Purge | cutoffs | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/purge_dups/cutoffs` | 18 B | 2026-04-08 07:49 |  |
| Reads | HiFi staged filt.fastq.gz | `/home/proj_202504p2_BD-MED/abner/durio/assembly/DurZibPV/results/pacbio/pacbio.filt.fastq.gz` | 28.37 GiB | 2026-04-07 23:54 |  |

**Likely missing (for pan-project parity)** — QUAST, seqkit stats output, purge_dups plot_hist.png, RagTag (not found), .cool/.mcool (not found), .pretext (not found).

---

## Global sample sheet

- `/home/proj_202504p2_BD-MED/abner/durio/samplesheet_hic.csv` — 379 B, modified 2026-02-04 23:02

---

## Regenerating this inventory

From the `durio` repository root:

```bash
python3 assembly/scripts/generate_qc_inventory.py
```

The script only scans directories under `assembly/` whose names start with `Dur` (twelve species in this snapshot).
