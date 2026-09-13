# H-005 Audit Sequence: Engine v0.7 → v0.8

## Status

This directory preserves the experimental artifacts from an audit sequence
in which two apparently compelling quantitative findings were subsequently
rejected after implementation review.

### Retained finding

The simulation shows a repeatable difference in ambiguity-resolution behavior:
the structural-vacuum condition relies substantially more on guessing and less
on formal resolution mechanisms.

Baseline miss rates remain broadly similar across conditions. The retained
finding therefore concerns process behavior, not underlying agent competence.

### Rejected finding: Engine v0.7

Engine v0.7 initially produced a large apparent difference in catastrophic
outcomes.

Audit showed that condition-specific treatment leakage routed one class of
outcomes into a permanently non-paying-down backlog. The result was rejected.

### Rejected metric: Engine v0.8

Engine v0.8 corrected the original treatment leakage and produced another
large apparent catastrophe-risk difference.

A subsequent self-audit found that the measured catastrophe pathway was
structurally unavailable to the control condition. The catastrophe metric
was therefore retired and is preserved here only as an audit artifact.

### Why preserve the rejected artifacts?

They document the evaluation process rather than merely its successful
outcomes.

The objective of this repository is to make experimental reasoning,
implementation errors, corrections, and bounded conclusions inspectable.

See the full case study:

[False-Positive Audit](../../case-study/false-positive-audit.md)

## Artifact Map

### Start here

- [v0.7 public results summary](h005_v0_7_results_summary_public.md)
  — documents the original false positive, the audit, and why the result was rejected.

- [v0.8 retrospective summary](h005_v0_8_retrospective_summary.md)
  — documents what survived the correction and the second self-audit.

### Raw evidence

- [v0.7 raw results](h005_v0_7_results.json)
- [v0.8 raw results](h005_v0_8_results.json)

### Historical analysis

- [v0.8 sensitivity analysis](v08_sensitivity.py)
  — preserved for audit provenance. It analyzes the catastrophe metric that was
  subsequently rejected for comparative inference.

### Engine source

- [v0.8 simulation engine](../../simulation/enterprise_sim_engine_v0_8.py)

The original v0.7 engine source will be added when the historical file is
recovered. It will not be reconstructed and presented as the original artifact.
