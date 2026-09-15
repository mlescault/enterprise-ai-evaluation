# Interactive Demo

[← Back to repository overview](../README.md)

This folder holds a self-contained, browser-based companion to the H-005 evidence in
this repository. It is a communication artifact, not new experimental evidence — the
same boundary that separates the [case study](../case-study/false-positive-audit.md)
and the [H-005 evidence directory](../experiments/h005-v07-v08/README.md) from the
underlying [v0.8 engine](../simulation/enterprise_sim_engine_v0_8.py) applies here too.

**Live:** once GitHub Pages is enabled for this repo (Settings → Pages → Deploy from
branch → `main` / `/docs`), this renders at `https://mlescault.github.io/enterprise-ai-evaluation/`.
Until then, open `index.html` directly in any browser — it has no server dependency.

To open straight to the readable tab instead of the default view, append `?tab=slice`
to the URL.

## What the four tabs are

**Live** — the published v0.8 engine's PM-vs-PdM decision logic, reimplemented in
JavaScript so it runs in the browser. Every run draws fresh randomness; it's meant to
be run several times to see the pattern, not read as a single citable trial.

**Recorded run (seed 3)** — one specific, real run of the actual Python engine
(`enterprise_sim_engine_v0_8.py`), captured via `capture_demo_trace.py` and frozen so
it can be pointed to and cited. Both conditions share an identical random seed, so
every ambiguous decision that comes up is exactly the same in both — only the
structural condition (`structural_rank_gap`, `pm_mandate_access`) differs. This is the
only tab where the retired catastrophe metric appears — see
[Boundary](#boundary-the-retired-catastrophe-metric) below.

**Escalation cascade** — a new extension built for this demo, not part of the
published engine. It reuses v0.8's real bid/mandate/backlog formulas but applies them
across an actual multi-tier structure (Pod Sync → Sprint Review → Pre-GM → GM meeting)
instead of one flat comparison, to show how far an unresolved disagreement travels up
the chain under each condition.

**Pod vertical slice** — one pod, thirteen sprint-goal issues, one meeting cycle. The
opening arguments for each issue are hand-written for this demo; whether an issue
aligns or escalates, and how far up the chain it travels, is computed using the same
bid/mandate/rank-gap math as the other tabs. Both conditions run on the identical
seeded random stream (seed 19 by default, citable; a "Reshuffle" control re-runs on
fresh randomness instead). Two issues are voiced in full — the one that's structurally
unresolvable at the pod level, and the highest-stakes issue Program actually loses
under the vacuum condition. The other eleven are computed in full and shown collapsed,
not hidden.

## Boundary: the retired catastrophe metric

The repository's own audit (see the root [README](../README.md) and the
[false-positive audit case study](../case-study/false-positive-audit.md)) found the
v0.8 catastrophe-comparison metric structurally invalid for comparative inference,
because the comparison condition could not enter the measured pathway. That finding is
not reversed here.

Live and Cascade do not compute a catastrophe threshold at all — that computation was
removed from the JavaScript entirely, not just hidden from the UI. Recorded still
displays the field, because it's a real value from the captured historical trace, but
it's explicitly labeled a retired metric and is not offered as a comparative finding.

## Provenance

`capture_demo_trace.py` instruments `run_pi()` in the real engine module to log
per-sprint events. It imports every constant and formula from
`enterprise_sim_engine_v0_8.py` rather than re-implementing them, so the Recorded
tab's numbers are exactly what v0.8 computed — the script only adds a log.
`demo_trace.json` is its raw output for `base_seed=3`, embedded directly in
`index.html`.

## Running locally

`index.html` is fully self-contained — all styles and logic are inline, and the only
external resource is a Google Fonts stylesheet (the page still renders correctly
without it, using a system font fallback). Open it directly in a browser, or serve the
folder with any static file server.
