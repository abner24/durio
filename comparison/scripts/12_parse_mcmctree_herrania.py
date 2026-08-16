#!/usr/bin/env python3
"""Parse Herrania MCMCtree mcmc.txt (ages in Ma + naive ESS)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import pandas as pd

from cluster_paths import MCMC_DIR


def ess(x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 10:
        return float("nan")
    x = x - x.mean()
    var = x.var(ddof=1)
    if var <= 0:
        return float(n)
    rho_sum = 0.0
    for lag in range(1, min(n // 3, 4000)):
        c = float(np.dot(x[:-lag], x[lag:]) / ((n - lag) * var))
        if c < 0.0:
            break
        rho_sum += c
    return n / (1.0 + 2.0 * rho_sum)


def main() -> None:
    run = MCMC_DIR / "herrania" / "posterior"
    mcmc = run / "mcmc.txt"
    if not mcmc.exists():
        raise SystemExit(f"missing {mcmc}")
    df = pd.read_csv(mcmc, sep=r"\s+").dropna()
    rows = []
    for col in df.columns:
        if not str(col).startswith("t_n"):
            continue
        v = df[col].to_numpy(dtype=float) * 100.0
        lo, hi = np.percentile(v, [2.5, 97.5])
        rows.append(
            {
                "node_id": col,
                "mean_Ma": float(v.mean()),
                "HPD2.5_Ma": float(lo),
                "HPD97.5_Ma": float(hi),
                "ESS": float(ess(df[col].to_numpy(dtype=float))),
                "n_samples": int(len(v)),
            }
        )
    ages = pd.DataFrame(rows)
    out = MCMC_DIR / "herrania" / "summary"
    out.mkdir(parents=True, exist_ok=True)
    ages.to_csv(out / "posterior_node_ages.tsv", sep="\t", index=False)
    tree = (run / "FigTree.tre").read_text() if (run / "FigTree.tre").exists() else ""
    meta = {
        "n_samples": int(len(df)),
        "min_ESS": float(ages["ESS"].min()) if len(ages) else None,
        "figtree": tree[:2000],
        "note": "Map t_n* onto FigTree.tre. Root should be cacao+Herrania vs Durio.",
    }
    (out / "posterior_ess.json").write_text(json.dumps(meta, indent=2) + "\n")
    print(ages.to_string(index=False))
    print(f"[OK] min ESS={meta['min_ESS']}")


if __name__ == "__main__":
    main()
