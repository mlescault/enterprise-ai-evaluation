# H-005 Engine v0.7 — Results and Caught Artifact

## Status

**Historical audit artifact. The headline result was rejected.**

Engine v0.7 ran 12 Program Increment cycles with N=50 seeds per cell.

## Initial Result

The first run produced a dramatic result in the wrong direction:

| Metric | Vacuum | Parity |
|---|---:|---:|
| Final cumulative catastrophe probability | 0.02 | 0.26 |
| Mean final backlog | 27.8 | 51.4 |
| Mean forced resolutions per seed | 0.8 | 3.7 |

Because the parity condition was intended to reduce structural ambiguity, this result was treated as a reason to inspect the implementation rather than as evidence.

## Audit Finding

The engine routed every wrong outcome produced through uncontested mandate use into a backlog pool that never paid down.

That conflated two different ideas:

- **uncontested** — a mandate assertion does not require negotiation; and
- **unreviewable** — no principal with institutional standing exists to revisit the decision.

Because mandate use occurred specifically in the parity condition, the implementation created a condition-specific pathway into permanently accumulating backlog.

This made the headline result an implementation artifact rather than evidence about organizational structure.

## Diagnostic Rerun

When mandate-wrong outcomes were routed into the same paydown-eligible backlog used for ordinary reviewable rework, the apparent difference disappeared:

| Metric | Vacuum | Parity |
|---|---:|---:|
| Final catastrophe probability | 0.02 | 0.02 |
| Mean final backlog | 27.8 | 27.4 |

**Conclusion: the original 0.02 vs. 0.26 difference was rejected.**

## What Survived

The process-level behavior remained meaningful:

- the vacuum condition relied more heavily on guessing;
- parity used formal resolution mechanisms more often;
- this did not establish a clean difference in catastrophic outcomes.

The v0.7 artifact therefore became an input to the next engine revision rather than a reported finding.

## Files

- `h005_v0_7_results.json` — raw recorded output from the historical run
- `enterprise_sim_engine_v0_7.py` — to be added when the original historical source is recovered
