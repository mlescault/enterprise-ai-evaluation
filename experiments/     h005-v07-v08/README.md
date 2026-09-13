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
