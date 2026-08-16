#!/bin/bash
# Run from the HPC clone of this repo (or from comparison/).
set -euo pipefail
ROOT="${DURIO_ROOT:-/home/proj_202504p2_BD-MED/abner/durio}"
CMP="${ROOT}/comparison"
mkdir -p "${CMP}/scripts" "${CMP}/logs"
# If this checkout is the HPC durio root, scripts are already here.
cd "${CMP}"
echo "submitting from $(pwd)"
qsub scripts/12_mcmctree_herrania.pbs
qsub scripts/15_jcvi.pbs
