# Comparative genomics jobs (HPC)

Scripts here are written for the cluster checkout at
`/home/proj_202504p2_BD-MED/abner/durio` (same `DURIO_ROOT` as `assembly/*/assembly.pbs`).
They are not runnable in the GitHub-only clone: OrthoFinder, BRAKER GFFs, proteomes,
and `wag.dat` live on the cluster and are not in this repo.

## Submit on the cluster

```bash
# after pulling this branch into the HPC clone
cd /home/proj_202504p2_BD-MED/abner/durio
mkdir -p comparison/scripts comparison/logs
# copy or git pull so comparison/scripts is present
cd comparison
qsub scripts/12_mcmctree_herrania.pbs
qsub scripts/15_jcvi.pbs
```

| Job | Script | Output |
|---|---|---|
| `durio_mcmcH` | `scripts/12_mcmctree_herrania.pbs` | `12_mcmctree/herrania/` — 10-taxon tree with *Herrania umbratica* sister to cacao; root 60–90 Ma; cacao–Herrania 5–20 Ma |
| `durio_jcvi` | `scripts/15_jcvi.pbs` | `15_jcvi/out/` — dual synteny + dotplots (MK vs PV, DatoAli, graveolens, Sin, Tes, Oxl, Suluk; Gra vs Mungkom) and a JCVI karyotype if `jcvi` imports |

Foreground dating taxa: cacao, Herrania, DurSin, DurTes, DurBru, DurOxl, DurDul, DurKut, DurGra_Og, T2T_MK_mat. Hybrids stay out of MCMCtree.

JCVI plots always write matplotlib PDFs/PNGs. Native `python -m jcvi.graphics.*` figures are extra when the `jcvi` package is available.
