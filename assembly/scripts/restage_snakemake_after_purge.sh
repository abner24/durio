#!/usr/bin/env bash
# Restage Snakemake after a manual purge_dups rerun so the workflow resumes
# from scaffolding / purged-assembly QC without re-running the purge_dups rules.
#
# Usage:
#   ./restage_snakemake_after_purge.sh /path/to/assembly/DurBru
#   ./restage_snakemake_after_purge.sh /path/to/assembly/DurBru --dry-run
#   ./restage_snakemake_after_purge.sh /path/to/assembly/DurBru --no-touch   # only remove stale outputs/metadata
#
# Requires: updated results/purge_dups/{assembly.purged.fasta,assembly.hap.fasta,purge_dups.bed,cutoffs}
# and the upstream purge intermediates (assembly.self.paf, pbcstat.*, etc.) from the original run.

set -euo pipefail

log() { echo "[$(date -Is)] $*"; }

usage() {
  sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'
  echo ""
  echo "Options:"
  echo "  --dry-run     Print actions without changing files"
  echo "  --no-backup   Do not move removed paths into results/_restage_backup_<timestamp>/"
  echo "  --no-touch    Skip 'snakemake --touch' (only remove downstream + metadata)"
  echo "  -h, --help    Show this help"
}

ASSEMBLY_ROOT=""
DRY_RUN=0
DO_BACKUP=1
DO_TOUCH=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --no-backup) DO_BACKUP=0; shift ;;
    --no-touch) DO_TOUCH=0; shift ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
    *)
      if [[ -z "${ASSEMBLY_ROOT}" ]]; then
        ASSEMBLY_ROOT="$1"
        shift
      else
        echo "Unexpected argument: $1" >&2; exit 2
      fi
      ;;
  esac
done

if [[ -z "${ASSEMBLY_ROOT}" ]]; then
  echo "ERROR: ASSEMBLY_ROOT required." >&2
  usage >&2
  exit 2
fi

ASSEMBLY_ROOT="$(cd "${ASSEMBLY_ROOT}" && pwd)"

SNAKEFILE="${SNAKEFILE:-/home/proj_202504p2_BD-MED/abner/GenomeAssembly/Snakefile}"
SNAKEMAKE_PROFILE="${SNAKEMAKE_PROFILE:-/home/proj_202504p2_BD-MED/abner/GenomeAssembly/config}"
SNAKEMAKE_EXTRA="${SNAKEMAKE_EXTRA:---use-conda}"

PURGE_DIR="${ASSEMBLY_ROOT}/results/purge_dups"
META_DIR="${ASSEMBLY_ROOT}/.snakemake/metadata"
INCOMPLETE_DIR="${ASSEMBLY_ROOT}/.snakemake/incomplete"

# Outputs produced by workflow/purge_dups.smk (mark complete via --touch).
PURGE_PIPELINE_OUTPUTS=(
  results/purge_dups/assembly.split.fa
  results/purge_dups/assembly.self.paf
  results/purge_dups/assembly.pacbio.paf
  results/purge_dups/pbcstat.cov
  results/purge_dups/pbcstat.stat
  results/purge_dups/cutoffs
  results/purge_dups/purge_dups.bed
  results/purge_dups/assembly.hap.fasta
  results/purge_dups/assembly.purged.fasta
  results/purge_dups/plot_hist.png
)

# Derived from assembly.purged.fasta (scaffolding.smk + index rules).
PURGE_DERIVED_OUTPUTS=(
  results/purge_dups/assembly.purged.fasta.fai
  results/purge_dups/assembly.purged.fasta.0123
  results/purge_dups/assembly.purged.fasta.amb
  results/purge_dups/assembly.purged.fasta.ann
  results/purge_dups/assembly.purged.fasta.bwt.2bit.64
  results/purge_dups/assembly.purged.fasta.pac
  results/purge_dups/assembly.purged.genome
)

# Hi-C scaffolding + curation (when hicF/hicR are set in asm_params.yaml).
HIC_OUTPUTS=(
  results/scaffolding
  results/curation
)

# Assembly QC on purged / scaffolded (workflow/qc.smk).
QC_PURGED_SCAFFOLDED=(
  results/qc/busco/purged
  results/qc/busco/scaffolded
  results/qc/merqury/purged
  results/qc/merqury/scaffolded
  results/qc/tidk/purged
  results/qc/tidk/scaffolded
  results/qc/genomescope/purged
  results/qc/genomescope/scaffolded
  results/qc/smudgeplot/purged_smudgeplot.pdf
)

# FastK k-mer DB fragments for purged/scaffolded (count_assembly_kmers).
QC_KMER_GLOBS=(
  "results/qc/kmers/purged*"
  "results/qc/kmers/scaffolded*"
  "results/qc/kmers/fastk_tmp_purged"
  "results/qc/kmers/fastk_tmp_scaffolded"
)

has_hic() {
  local params="${ASSEMBLY_ROOT}/asm_params.yaml"
  [[ -f "${params}" ]] || return 1
  grep -qE '^hicF:[[:space:]]*[^[:space:]]' "${params}" \
    && grep -qE '^hicR:[[:space:]]*[^[:space:]]' "${params}"
}

metadata_b64() {
  printf '%s' "$1" | base64 -w0 2>/dev/null || printf '%s' "$1" | base64 | tr -d '\n'
}

remove_metadata_for_path() {
  local rel="$1"
  local f="${META_DIR}/$(metadata_b64 "${rel}")"
  if [[ -f "${f}" ]]; then
    if [[ "${DRY_RUN}" -eq 1 ]]; then
      log "[dry-run] rm metadata $(basename "${f}")  # ${rel}"
    else
      rm -f "${f}"
    fi
  fi
}

remove_metadata_prefix() {
  local prefix="$1"
  [[ -d "${META_DIR}" ]] || return 0
  local f rel
  for f in "${META_DIR}"/*; do
    [[ -f "${f}" ]] || continue
    rel="$(basename "${f}" | base64 -d 2>/dev/null || true)"
    [[ -n "${rel}" ]] || continue
    if [[ "${rel}" == "${prefix}"* ]]; then
      if [[ "${DRY_RUN}" -eq 1 ]]; then
        log "[dry-run] rm metadata $(basename "${f}")  # ${rel}"
      else
        rm -f "${f}"
      fi
    fi
  done
}

remove_incomplete_for_path() {
  local rel="$1"
  local f="${INCOMPLETE_DIR}/$(metadata_b64 "${rel}")"
  if [[ -f "${f}" ]]; then
    if [[ "${DRY_RUN}" -eq 1 ]]; then
      log "[dry-run] rm incomplete $(basename "${f}")  # ${rel}"
    else
      rm -f "${f}"
    fi
  fi
}

stage_remove() {
  local target="$1"
  local abs="${ASSEMBLY_ROOT}/${target}"
  if [[ ! -e "${abs}" ]]; then
    return 0
  fi
  if [[ "${DO_BACKUP}" -eq 1 && -n "${BACKUP_ROOT:-}" ]]; then
    local dest="${BACKUP_ROOT}/${target}"
    if [[ "${DRY_RUN}" -eq 1 ]]; then
      log "[dry-run] backup ${target} -> ${dest}"
    else
      mkdir -p "$(dirname "${dest}")"
      if [[ -d "${abs}" ]]; then
        mkdir -p "${dest}"
        cp -a "${abs}/." "${dest}/"
      else
        cp -a "${abs}" "${dest}"
      fi
    fi
  fi
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "[dry-run] rm -rf ${target}"
  else
    rm -rf "${abs}"
  fi
}

# ── checks ────────────────────────────────────────────────────────────────────

log "ASSEMBLY_ROOT=${ASSEMBLY_ROOT}"

for need in \
  results/purge_dups/assembly.purged.fasta \
  results/purge_dups/assembly.hap.fasta \
  results/purge_dups/purge_dups.bed \
  results/purge_dups/cutoffs \
  results/purge_dups/assembly.self.paf \
  results/purge_dups/pbcstat.cov \
  results/purge_dups/pbcstat.stat; do
  [[ -f "${ASSEMBLY_ROOT}/${need}" ]] || {
    log "ERROR: missing ${need} — run purge_dups first."
    exit 1
  }
done

if [[ ! -f "${ASSEMBLY_ROOT}/asm_params.yaml" ]]; then
  log "WARN: asm_params.yaml not found; assuming Hi-C is enabled for cleanup."
  HIC_ENABLED=1
elif has_hic; then
  HIC_ENABLED=1
  log "Hi-C inputs found in asm_params.yaml — will clear scaffolding/curation."
else
  HIC_ENABLED=0
  log "No Hi-C in asm_params.yaml — skipping scaffolding/curation cleanup."
fi

if [[ "${DO_BACKUP}" -eq 1 ]]; then
  BACKUP_ROOT="${ASSEMBLY_ROOT}/results/_restage_backup_$(date +%Y%m%d_%H%M%S)"
  log "Backup root: ${BACKUP_ROOT}"
fi

# ── remove stale downstream ───────────────────────────────────────────────────

log "Removing downstream outputs and Snakemake metadata..."

for rel in "${PURGE_DERIVED_OUTPUTS[@]}"; do
  remove_metadata_for_path "${rel}"
  remove_incomplete_for_path "${rel}"
  stage_remove "${rel}"
done

if [[ "${HIC_ENABLED}" -eq 1 ]]; then
  for rel in "${HIC_OUTPUTS[@]}"; do
    remove_metadata_prefix "${rel}"
    stage_remove "${rel}"
  done
fi

for rel in "${QC_PURGED_SCAFFOLDED[@]}"; do
  remove_metadata_prefix "${rel}"
  stage_remove "${rel}"
done

shopt -s nullglob
for pattern in "${QC_KMER_GLOBS[@]}"; do
  for abs in "${ASSEMBLY_ROOT}/${pattern}"; do
    rel="${abs#${ASSEMBLY_ROOT}/}"
    remove_metadata_for_path "${rel}"
    remove_incomplete_for_path "${rel}"
    stage_remove "${rel}"
  done
done
shopt -u nullglob

# Unlock a previous failed Snakemake run if present.
if [[ -d "${ASSEMBLY_ROOT}/.snakemake/locks" ]] \
  && compgen -G "${ASSEMBLY_ROOT}/.snakemake/locks/*" > /dev/null; then
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "[dry-run] snakemake --unlock"
  elif command -v snakemake >/dev/null 2>&1; then
    (
      cd "${ASSEMBLY_ROOT}"
      snakemake -s "${SNAKEFILE}" --profile "${SNAKEMAKE_PROFILE}" --unlock
    ) || log "WARN: snakemake --unlock failed (locks may already be clear)."
  else
    log "WARN: snakemake not on PATH; remove .snakemake/locks/* manually if a run was interrupted."
  fi
fi

# ── register manual purge outputs with Snakemake ──────────────────────────────

touch_targets=()
for rel in "${PURGE_PIPELINE_OUTPUTS[@]}"; do
  if [[ -f "${ASSEMBLY_ROOT}/${rel}" ]]; then
    touch_targets+=("${rel}")
  fi
done

if [[ "${DO_TOUCH}" -eq 1 ]]; then
  if [[ ${#touch_targets[@]} -eq 0 ]]; then
    log "ERROR: no purge pipeline outputs found to touch."
    exit 1
  fi
  if [[ "${DRY_RUN}" -eq 1 ]]; then
    log "[dry-run] snakemake --touch ${touch_targets[*]}"
  else
    if ! command -v snakemake >/dev/null 2>&1; then
      log "ERROR: snakemake not on PATH (needed for --touch)."
      exit 1
    fi
    log "snakemake --touch (${#touch_targets[@]} purge outputs)..."
    # shellcheck disable=SC2086
    (
      cd "${ASSEMBLY_ROOT}"
      snakemake -s "${SNAKEFILE}" \
        --profile "${SNAKEMAKE_PROFILE}" \
        ${SNAKEMAKE_EXTRA} \
        --touch \
        "${touch_targets[@]}"
    )
  fi
else
  log "Skipping snakemake --touch (--no-touch)."
fi

# ── resume instructions ───────────────────────────────────────────────────────

log "Done."
cat <<EOF

Next: resume the GenomeAssembly workflow from ${ASSEMBLY_ROOT}:

  cd ${ASSEMBLY_ROOT}
  snakemake -s ${SNAKEFILE} \\
    --profile ${SNAKEMAKE_PROFILE} \\
    ${SNAKEMAKE_EXTRA} \\
    --jobs 20

Snakemake should skip purge_dups rules and rebuild scaffolding, purged/scaffolded QC,
and curation (if Hi-C is configured). Initial-assembly QC (initial BUSCO/Merqury/tidk)
is left untouched.

Optional: force only downstream branches without deleting files first:
  snakemake ... --forcerun samtools_faidx --forcerun bwa_mem2_index_hifiasm

EOF
