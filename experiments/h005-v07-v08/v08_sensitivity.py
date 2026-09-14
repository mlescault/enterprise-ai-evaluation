# PUBLICATION NOTE
# Historical sensitivity analysis for the v0.8 catastrophe metric.
# This metric was subsequently determined to be structurally invalid for
# comparative inference and is not retained as a finding.
# Preserved for audit provenance only.
#
# See: h005_v0_8_retrospective_summary.md

"""
Sensitivity checks on the v0.8 K=12 headline result (vacuum 0.35 vs parity 0.02,
z=12.0, p<0.0001, N=400/cell) before treating it as a finding rather than
another artifact of a single hardcoded constant.

Two things are varied independently, holding the vacant-seat gating logic itself
fixed (that's the mechanism under test, not what's being sensitivity-checked
here):

  1. CATASTROPHE_MIN_CAPACITY_FRACTION -- the threshold debt flagged since v0.6b,
     never stress-tested. Checked at 0.10 / 0.15 (headline) / 0.20.
  2. UNREVIEWABLE_PAYDOWN_RATE -- headline run assumes a vacant seat's backlog
     NEVER pays down (rate=0.0), which is the strongest possible version of
     "no one ever revisits it." Checked against a much weaker assumption
     (0.05/PI -- a vacant seat's backlog still heals 4x slower than an ordinary
     seat's 0.20/PI, but isn't literally permanent) to see whether the gap
     survives relaxing the strongest-case assumption.

N dropped to 150/cell here (robustness scan, not the headline estimand) to
keep this fast; the two central cells (vacuum, parity) are what's compared.
"""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
SIMULATION_DIR = REPO_ROOT / "simulation"
sys.path.insert(0, str(SIMULATION_DIR))

import random
import importlib
import enterprise_sim_engine_v0_8 as eng

N_SEEDS_SCAN = 150


def run_pair(label):
    conditions = eng.build_factorial()
    vac, _, _, par = conditions
    vac_r = eng.run_cell(vac, N_SEEDS_SCAN, base_seed=9001, k_pis=12)
    par_r = eng.run_cell(par, N_SEEDS_SCAN, base_seed=9002, k_pis=12)
    z, p = eng.two_prop_z_test(
        vac_r["catastrophe_count"],
        vac_r["n_seeds"],
        par_r["catastrophe_count"],
        par_r["n_seeds"],
    )
    print(
        f"{label}: vacuum={vac_r['final_cumulative_catastrophe_prob']:.3f} "
        f"({vac_r['catastrophe_count']}/{vac_r['n_seeds']})  "
        f"parity={par_r['final_cumulative_catastrophe_prob']:.3f} "
        f"({par_r['catastrophe_count']}/{par_r['n_seeds']})  "
        f"z={z:.2f} p={p:.4f}"
    )


print("=== Threshold sensitivity (UNREVIEWABLE_PAYDOWN_RATE fixed at 0.0) ===")
for frac in (0.10, 0.15, 0.20):
    eng.CATASTROPHE_MIN_CAPACITY_FRACTION = frac
    run_pair(f"threshold={frac}")
eng.CATASTROPHE_MIN_CAPACITY_FRACTION = 0.15  # restore headline value

print()
print("=== Unreviewable-paydown sensitivity (threshold fixed at 0.15) ===")
for rate in (0.0, 0.05, 0.20):
    eng.UNREVIEWABLE_PAYDOWN_RATE = rate
    run_pair(f"unreviewable_paydown_rate={rate}")
eng.UNREVIEWABLE_PAYDOWN_RATE = 0.0  # restore headline value
