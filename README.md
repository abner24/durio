# durio

Genome assembly project configs and QC summaries for *Durio* species.

- **Workflow code:** [GenomeAssembly](https://github.com/abner24/GenomeAssembly) (Snakemake) — pin the commit used for each run in `assembly/<species>/`.
- **Large files** (reads, FASTAs, BAMs, FastK `.ktab` databases) stay on cluster / archival storage; not in this repo.
- **Tracked summaries:** per-species `results/pre_assembly/` (GenomeScope, smudgeplot) and `results/qc/` (BUSCO, Merqury, tidk, assembly GenomeScope).
- **Tracked organelles:** `results/organelles/oatk.{pltd,mito}.ctg.fasta`, BEDs, and annotation tables (~120 MB total). Large OATK unitig graphs (`oatk.utg*.gfa`) are excluded.

## Run assembly (example)

```bash
cd assembly/DurZibPV
qsub assembly.pbs
```

See `assembly/scripts/` for manual purge rerun and Snakemake restaging.
