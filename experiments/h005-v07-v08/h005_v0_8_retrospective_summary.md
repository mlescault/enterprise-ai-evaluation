# H-005 Engine v0.8 — Retrospective Audit Summary

## Status

**Historical experiment with a retained behavioral finding and a rejected catastrophe metric.**

Engine v0.8 corrected the treatment leakage discovered in v0.7 and reran the factorial experiment at N=400 seeds per cell over 12 Program Increment cycles.

A later self-audit found that the replacement catastrophe metric still had a structural validity problem. The raw results are preserved for inspection, but that catastrophe result is not treated as a retained finding.

## What v0.8 Corrected

v0.8 stopped routing ordinary mandate-driven errors into a permanently non-paying-down backlog.

Instead, the engine tied the special backlog state to:

`principal_seat_vacant = structural_rank_gap AND pm_mandate_access == "none"`

This removed the original v0.7 treatment-leakage defect.

## Result That Survived Audit

The strongest retained result is a difference in how ambiguity was resolved, not a difference in baseline competence.

At K=12:

| Metric | Vacuum | Parity |
|---|---:|---:|
| Mean guesses per seed | 6.165 | 4.06 |
| Mean forced resolutions per seed | 0.7525 | 3.7375 |
| Mean misses per seed | 2.2225 | 2.2625 |

The miss rates are very similar, while the resolution behavior differs substantially.
`decision_value` never sees condition, so similar miss totals are expected by
construction; the resolution-behavior difference is the measured result.

**Bounded interpretation:** the simulated governance structure changes how agents respond to ambiguity. It does not show that one condition contains intrinsically more competent agents.

## Metric Rejected After Self-Audit

The v0.8 engine also produced a large apparent difference in cumulative catastrophe probability.

That result was later rejected as a valid comparative finding.

The catastrophe pathway depended on `principal_seat_vacant`, which by construction is only true in the Vacuum cell. The control condition therefore could not enter the same counted pathway.

A zero or near-zero control value could not be interpreted as evidence that the control handled the same risk better; the outcome eligibility itself was asymmetric.

The catastrophe metric is preserved only as an audit artifact.

## Consequence

The successor design requires the same consequence pathway to be available in every experimental condition. Treatments may alter transition probabilities, but they may not determine which outcomes are eligible to occur or be counted.

## Files

- `h005_v0_8_results.json` — raw recorded output
- `enterprise_sim_engine_v0_8.py` — public-release copy of the historical engine with publication note
- `v08_sensitivity.py` — historical sensitivity analysis of the subsequently rejected catastrophe metric; retained only for audit provenance
