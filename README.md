# Enterprise AI Evaluation

A work-in-progress experimental environment for studying organizational behavior,
decision-making, coordination, and evaluation integrity in complex software-development
organizations.

I originally built this simulation to test practitioner hypotheses about how software
organizations respond to ambiguity, dependencies, governance pressure, and capacity
constraints.

An early experiment strongly supported one of my own hypotheses. That result triggered
additional scrutiny. I found treatment leakage, rejected the result, corrected the
experiment, reran it, and then found and rejected a second structurally invalid outcome
metric.

The most important artifact in this repository is therefore not a particular number.
It is the audit trail showing how apparently strong evidence was tested, rejected where
invalid, and narrowed to what remained supportable.

[Reviewer Guide](REVIEW_GUIDE.md) — fastest path through the evidence.

---

## Evidence at a Glance

**Executed and audited**  
H-005 v0.7 → v0.8 rule-based organizational simulation and audit sequence.

**Rejected**  
The original v0.7 headline result and the later v0.8 catastrophe comparison.

**Retained**  
A bounded behavioral observation: the experimental conditions produced different
ambiguity-resolution behavior, particularly in the balance between guessing and
forcing formal resolution, while observed miss rates remained similar.

**Prospective / not yet executed**  
H-006 capacity-orchestration experiment. Architecture and integrity-gate direction
are defined, but preregistration is still in progress and baseline execution remains
blocked pending unresolved parameters and statistical planning.

**Future / not yet implemented**  
Configurable organizational structures and heterogeneous production-LLM agents.

---

## Current Technical Scope

The currently published engines are **rule-based stochastic organizational
simulations**.

They do **not currently call production LLMs** and should not be interpreted as a
production LLM-agent evaluation harness.

The current work focuses on establishing and auditing the organizational
experimental layer:

- roles and authority;
- dependencies and ambiguity;
- capacity and commitments;
- governance and escalation;
- treatment boundaries;
- outcome measurement;
- experimental integrity.

The longer-term research direction includes configurable organizations,
heterogeneous LLM-powered agents, hidden model identity, agent mobility, and
model × role × organization experiments.

That work is planned, not executed.

See [ROADMAP.md](ROADMAP.md) for the full research direction and development roadmap.

---

## For Reviewers

### If you have about 60 seconds

Open the [interactive vertical slice](https://mlescault.github.io/enterprise-ai-evaluation/?tab=slice) —
one pod, thirteen sprint-goal issues, one meeting cycle, computed live in the browser
from the same v0.8 bid/mandate/rank-gap logic as the executed evidence below. No setup,
nothing to read first.

### If you have about 2 minutes

Read:

1. This README.
2. [REVIEW_GUIDE.md](REVIEW_GUIDE.md).

### If you have about 5 minutes

Read:

1. [False-Positive Audit Case Study](case-study/false-positive-audit.md)
2. [H-005 Experiment Artifacts](experiments/h005-v07-v08/README.md)

### If you want to inspect implementation and raw evidence

Review:

1. [v0.8 Simulation Engine](simulation/enterprise_sim_engine_v0_8.py)
2. [H-005 Raw Results and Audit Artifacts](experiments/h005-v07-v08/README.md)
3. [H-006 Prospective Design](prospective-research/H006/README.md)

---

## What This Demonstrates

This repository currently demonstrates:

- adversarial evaluation of a rule-based organizational simulation;
- detection and rejection of treatment leakage;
- detection and rejection of structurally invalid comparative metrics;
- separation of retained findings from rejected results;
- preservation of failed and rejected work as part of the audit trail;
- prospective experimental design and integrity-gate development;
- translation of enterprise software-domain expertise into testable scenarios;
- bounded interpretation of evidence.

The current simulation is primarily an **experimental-methodology and evaluation
work sample**, not evidence of a completed production LLM-agent system.

---

## H-005: Executed Audit Sequence

The H-005 sequence is the primary executed evidence in this repository.

The process was:

1. Form a falsifiable practitioner hypothesis.
2. Execute the experiment.
3. Obtain a strong confirming result.
4. Treat that confirmation as a reason for additional scrutiny.
5. Discover treatment leakage.
6. Reject the headline result.
7. Correct the experimental plumbing.
8. Rerun at larger sample size.
9. Audit the correction.
10. Discover a second structural measurement flaw.
11. Retire that metric.
12. Preserve only the narrower observation still supported by the evidence.

### Retained Observation

After correction, the two conditions continued to exhibit different
ambiguity-resolution behavior.

The vacuum condition guessed more frequently and forced formal resolution less
frequently, while observed miss rates remained similar.

This is retained as a **behavioral observation**.

Per-call correctness is scored the same way regardless of condition — the
engine's decision function never sees which condition is running — so the
similar miss totals are an expected consequence of that shared scoring, not a
measured finding about judgment quality.

It is not presented as evidence that one condition was globally more competent,
more effective, or more successful than the other.

### Rejected Results

Two stronger-looking results are explicitly not retained.

**v0.7 headline result**  
Rejected after audit found treatment leakage that allowed one condition to route
outcomes through a structurally different pathway.

**v0.8 catastrophe comparison**  
Rejected after audit found that the measured catastrophe pathway was structurally
unavailable to the control condition.

The underlying artifacts remain available because rejected evidence is part of the
experimental history.

See:

- [False-Positive Audit Case Study](case-study/false-positive-audit.md)
- [H-005 Evidence Directory](experiments/h005-v07-v08/README.md)

---

## H-006: Prospective Work

H-006 is intended to move experimental-integrity controls earlier in the lifecycle.

Rather than discovering treatment or measurement asymmetries after results appear,
the design introduces stronger pre-execution parameter controls, treatment-boundary
checks, and integrity gates.

H-006 has **not been executed**.

Its architecture and integrity-gate direction are defined, but preregistration is
still in progress. Baseline execution remains blocked until unresolved parameters
and the statistical plan are complete.

H-006 should therefore be interpreted as evidence of prospective experimental
design discipline, not as an experimental finding.

See:

- [H-006 Overview](prospective-research/H006/README.md)
- [H-006 Specification](prospective-research/H006/H006_SPEC_FREEZE_1.md)
- [H-006 Parameter Registry](prospective-research/H006/H006_BASELINE_PARAMETER_REGISTRY_1.md)

---

## Repository Evidence

### Simulation

Current published engine:

[enterprise_sim_engine_v0_8.py](simulation/enterprise_sim_engine_v0_8.py)

The public-release version changes the original environment-specific output path
to a repository-relative path. Simulation logic is otherwise preserved for audit
purposes.

See [simulation/README.md](simulation/README.md).

### Interactive Demo

A browser-based companion that renders the same H-005 conditions as a readable
negotiation trace, with the retired catastrophe metric confined to historical
display only. Start with the vertical slice — it's the most readable and most
citable of the four tabs.

[Open the vertical slice](https://mlescault.github.io/enterprise-ai-evaluation/?tab=slice) · [Browse the demo docs](docs/README.md)

### H-005 Results

The H-005 evidence directory contains:

- raw v0.7 result data;
- retrospective documentation of the rejected v0.7 result;
- raw v0.8 result data;
- retrospective v0.8 audit documentation;
- historical sensitivity analysis;
- links to the public v0.8 engine.

[Browse H-005 evidence](experiments/h005-v07-v08/README.md)

### Historical v0.7 Source

The original historical `enterprise_sim_engine_v0_7.py` source has not yet been
recovered from the original working environment.

It will not be reconstructed and presented as historical source.

When the original file is recovered, it will be added as an audit artifact.

This is an explicit limitation of the current repository.

---

## Scope and Limitations

The current simulation is a synthetic organizational model.

It is **not an empirically calibrated model of a specific company, workforce, or
AI system**.

Numeric parameters are used to test experimental mechanics and behavioral
hypotheses. They should not be interpreted as measured real-world effect sizes.

The project distinguishes three categories:

**Current executed evidence**  
Rule-based organizational simulation and adversarial experimental auditing.

**Current prospective work**  
H-006 and continued development of stronger pre-execution integrity controls.

**Future research direction**  
Configurable organizations populated by heterogeneous LLM-powered agents, with
model identity retained as experimental metadata but hidden from participating
agents.

See [ROADMAP.md](ROADMAP.md).

---

## Evaluation Principle

The purpose of this project is not to prove that one management approach,
organizational structure, or AI model is superior to another.

The goal is to make assumptions visible, measurements reproducible, rejected
results inspectable, and observations separable from interpretation.

Where the evidence supports only a narrow observation, the project should report
only that observation.

Others should be free to examine the same evidence and draw different conclusions.

---

## Project Status

**H-005:** Executed, audited, and retrospectively documented.

**H-005 v0.7 headline result:** Rejected.

**H-005 v0.8 ambiguity-resolution observation:** Retained with bounded
interpretation.

**H-005 v0.8 catastrophe comparison:** Rejected.

**H-006:** Prospective design / preregistration in progress. Baseline not yet
executed.

**Heterogeneous production LLM agents:** Planned future milestone. Not yet
implemented.

**Generalized user-configurable organizational structures:** Planned.

---

## Longer-Term Research Direction

The longer-term project aims to become a configurable environment for studying
how heterogeneous AI systems behave inside persistent organizations.

That research vision is intentionally separated from the executed evidence in
this README.

For the full research mission, source-of-truth principles, heterogeneous-model
design, agent-mobility questions, and development phases, see:

**[ROADMAP.md](ROADMAP.md)**
