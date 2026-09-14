# Simulation Engines

[← Back to repository overview](../README.md)

This directory contains executable simulation engines supporting the enterprise AI evaluation case studies in this repository.

## Current Status

### Engine v0.8

The public-release copy of Engine v0.8 is available here:

- [enterprise_sim_engine_v0_8.py](enterprise_sim_engine_v0_8.py)

The engine is preserved as part of the H-005 audit trail. Its publication note identifies a later-discovered measurement problem: the catastrophe metric implemented in this historical version was subsequently determined to be structurally invalid for comparative inference and is not reported as a retained finding.

The retained v0.8 finding concerns differences in ambiguity-resolution behavior, not differences in underlying agent competence or catastrophic outcomes.

## Running v0.8

From the repository root:

```bash
python simulation/enterprise_sim_engine_v0_8.py
```

The engine uses only the Python standard library and writes its result file to the current working directory.

### Engine v0.7

The original v0.7 engine source has not yet been recovered for publication.

The v0.7 raw results and retrospective audit summary are already available in the experiment archive. The historical source will be added when the original file is recovered; it will not be reconstructed and presented as the original artifact.

## Supporting Evidence

The full v0.7 → v0.8 audit sequence, raw results, retrospective summaries, and historical sensitivity analysis are available here:

- [H-005 audit artifacts](../experiments/h005-v07-v08/)
- [False-positive audit case study](../case-study/false-positive-audit.md)

## Important Scope Note

These engines are rule-based stochastic organizational simulations.

They do not currently call production LLMs or represent a production LLM-agent evaluation harness.

Their role in this repository is to demonstrate experimental design, adversarial auditing, treatment isolation, falsifiability, and bounded interpretation of results.
