# Enterprise AI Evaluation

A configurable experimental environment for studying organizational behavior,
decision-making, coordination, and eventually heterogeneous AI agents inside
complex software-development organizations.

I originally built this simulation to test practitioner hypotheses about how
software organizations respond to ambiguity, dependencies, governance pressure,
and capacity constraints.

When an early result strongly supported one of my own hypotheses, I audited the
implementation, discovered that the result was being produced in part by treatment
leakage, rejected it, corrected the experiment, and then found and rejected a second
structurally invalid outcome metric.

That experience changed the purpose of the project.

The goal is not to build a simulation that confirms management theories or produces
a preferred answer. The goal is to build an increasingly trustworthy experimental
environment in which organizational behavior can be observed, measured, audited,
and reproduced.

**Current evidence is based on rule-based stochastic simulation. Production LLMs
have not yet been integrated into the organizational simulation.**

[Reviewer Guide](REVIEW_GUIDE.md) — the fastest path through the evidence.

---

## Current Technical Scope

The currently published simulation engines are **rule-based stochastic
organizational simulations**.

They do **not currently call production LLMs** and should not be interpreted as a
production LLM-agent evaluation harness.

The current work establishes and audits the organizational simulation layer:

- roles and authority;
- dependencies and ambiguity;
- capacity and commitments;
- governance and escalation;
- treatment boundaries;
- outcome measurement;
- experimental integrity.

This foundation is intentional.

Before introducing model behavior, the project aims to make the surrounding
experimental environment as inspectable and reliable as possible.

---

## Research Mission

The long-term goal is to create a configurable organizational laboratory that
researchers and practitioners can adapt to their own structures, roles,
constraints, and research questions.

Rather than hard-coding a single organization, the simulation should eventually
allow a user to define an organizational structure — hierarchy, disciplines,
reporting relationships, team composition, dependencies, operating rules, and
other relevant constraints — and then observe how that system behaves under
controlled experimental conditions.

A major planned milestone is the introduction of **heterogeneous LLM-powered
agents**.

Each simulated individual would be powered by a model randomly selected from a
pool of AI systems. The simulation would retain that model assignment as
experimental metadata, while model identity would remain hidden from the
participating agents.

In that design:

- an agent would not know which model powers itself;
- an agent would not know which models power other agents;
- model assignments would vary across simulation seeds;
- organizational role, authority, incentives, information, and relationships
  would remain distinct from model identity.

With agent mobility enabled, this would make it possible to observe whether
behavioral similarities lead agents to cluster, separate, form more effective
teams, create greater friction, or produce other patterns that were not explicitly
programmed into the system.

The purpose is not to predict those outcomes in advance.

**The purpose is to create an environment capable of measuring them if they emerge.**

---

## Source-of-Truth Principles

This project is intended to produce observations, not preferred conclusions.

The simulator inevitably contains modeling assumptions. The goal is therefore not
to claim perfect objectivity, but to make assumptions explicit, measurements
reproducible, and interpretation separable from observation.

The project follows several operating principles:

- **No preferred outcome.** Experimental design should not encode the conclusion
  the experiment is expected to produce.
- **Expose assumptions.** Role definitions, treatments, parameters, measurement
  rules, and known limitations should remain visible.
- **Preserve rejected results.** False positives, invalid metrics, and failed
  experiments are part of the audit trail rather than artifacts to be hidden.
- **Separate observation from interpretation.** The project should report what
  was measured and under what conditions without extending claims beyond the
  evidence.
- **Bound conclusions.** If the evidence supports only a narrow observation,
  report only the narrow observation.
- **Prefer reproducibility over persuasion.** Another researcher should be able
  to inspect the conditions, artifacts, and reasoning that produced a result.
- **Treat confirmation as a reason for scrutiny.** Results that strongly confirm
  an evaluator's prior belief deserve at least as much auditing as surprising
  results.

The desired outcome is an increasingly reliable source of experimental evidence
that others can analyze, challenge, reinterpret, extend, or build upon.

---

## Long-Term Research Direction

The project is intended to evolve from a validated organizational simulation into
a platform for studying heterogeneous AI systems operating inside persistent
organizations.

Potential research dimensions include:

- model family × organizational role;
- model family × organizational level;
- homogeneous versus heterogeneous team composition;
- negotiation, escalation, and conflict behavior;
- ambiguity resolution and dependency management;
- trust formation and decay;
- agent mobility and emergent clustering;
- local team performance versus organization-wide outcomes;
- short-term efficiency versus long-term resilience;
- behavior under stress, changing priorities, and incomplete information.

The important unit of analysis is not necessarily the individual model.

A model that performs well in one role may perform differently in another. A model
that performs strongly in isolation may interact poorly with certain peers. A
heterogeneous team may outperform a homogeneous team under one governance
structure and underperform under another.

The project is designed to preserve the possibility that the most interesting
findings will be ones that were not anticipated when the experiment was created.

---

## Development Roadmap

### Phase 1 — Validate the Organizational Laboratory

**Current / ongoing**

Establish reproducible simulation mechanics, clean treatment boundaries,
auditable outcome measures, explicit assumptions, and preserved experimental
history.

H-005 is the primary executed audit case.

H-006 is prospective work intended to move experimental integrity controls
earlier in the lifecycle.

### Phase 2 — Generalize Organizational Structure

**Planned**

Move organizational structure out of hard-coded assumptions and into
configurable data.

The long-term target is to support substantially different organizations:
small studios, functional hierarchies, matrix organizations, platform teams,
distributed development groups, and other structures defined by the researcher.

### Phase 3 — Expand Persistent Organizational Behavior

**Planned**

Develop richer mechanisms for agent mobility, tenure, organizational memory,
trust, influence, dependencies, changing responsibilities, and longitudinal
consequences.

### Phase 4 — Introduce Heterogeneous LLM-Powered Agents

**Planned / not yet implemented**

Allow individual agents to use randomly assigned models from a heterogeneous
LLM pool.

Model identity remains hidden from participating agents while being retained
by the simulator as experimental metadata.

Assignments vary across seeds so that model effects can be distinguished from
individual placement and organizational circumstance.

### Phase 5 — Study Model × Role × Organization Interactions

**Future research**

Measure whether model families exhibit different patterns across roles, levels,
peer compositions, governance systems, and operating conditions.

The objective is not to produce a universal model leaderboard.

The objective is to publish the conditions and measurements needed for others
to evaluate those differences.

### Phase 6 — Reusable Organizational-Agent Research Platform

**Long-term goal**

Enable researchers and practitioners to define their own organizational
structures, agent populations, model pools, stressors, and measurement
questions while preserving experimental auditability and reproducibility.

Success would mean that others can use the platform to ask questions the
original project was never designed to answer — and take the work in directions
its creator did not anticipate.

---

## What This Demonstrates

This repository currently demonstrates:

- adversarial evaluation of a multi-agent organizational simulation;
- detection and rejection of treatment leakage;
- detection and rejection of structurally invalid comparative metrics;
- separation of retained findings from rejected results;
- prospective experimental design and integrity-gate development;
- translation of enterprise software-domain expertise into testable scenarios;
- preservation of failed and rejected work as part of the experimental record;
- explicit separation of current evidence from future LLM-agent research.

The current simulation should be viewed primarily as an **experimental and
evaluation-methodology work sample**, not as evidence of a completed production
LLM-agent system.

---

## Evidence Status

### Executed and Audited

**H-005 v0.7 → v0.8 audit sequence**

The original experiment produced a strong result that supported the practitioner
hypothesis.

Audit subsequently identified treatment leakage that created a structurally
different outcome pathway between experimental conditions.

That headline result was rejected.

The experiment was corrected and rerun at larger sample size.

A narrower behavioral finding survived:

> The experimental conditions produced different ambiguity-resolution behavior,
> particularly in the balance between guessing and forcing formal resolution,
> while observed miss rates remained similar.

This is retained as a **behavioral observation**, not evidence that one condition
was globally more competent or organizationally superior.

See:

- [H-005 experiment artifacts](experiments/h005-v07-v08/README.md)
- [False-positive audit case study](case-study/false-positive-audit.md)

### Rejected

Two major results are explicitly **not retained as findings**.

**H-005 v0.7 headline outcome**

Rejected because treatment leakage allowed one condition to route outcomes through
a structurally different pathway.

**H-005 v0.8 catastrophe comparison**

Rejected because the measured catastrophe pathway was structurally unavailable
to the control condition.

The underlying artifacts remain in the repository for audit provenance.

### Prospective / Not Yet Executed

**H-006 — Capacity-Orchestration Consequence Governance**

H-006 is a prospective design intended to apply lessons from the H-005 audit
before execution rather than after results appear.

Its architecture and integrity-gate direction are defined, but preregistration
is still in progress.

Baseline execution is blocked until unresolved parameters and the statistical
plan are complete.

H-006 should therefore be interpreted as evidence of prospective experimental
design discipline, **not as an executed result**.

See:

- [H-006 overview](prospective-research/H006/README.md)
- [H-006 specification](prospective-research/H006/H006_SPEC_FREEZE_1.md)
- [H-006 parameter registry](prospective-research/H006/H006_BASELINE_PARAMETER_REGISTRY_1.md)

---

## H-005 Audit Sequence

The most important artifact in the repository is not any single numeric result.

It is the audit sequence:

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
12. Preserve only the narrower observation that remains supported.

This sequence is documented because evaluation integrity is itself one of the
primary subjects of the project.

[Read the case study](case-study/false-positive-audit.md)

---

## Repository Evidence

### Simulation

The current public-release simulation engine is:

[simulation/enterprise_sim_engine_v0_8.py](simulation/enterprise_sim_engine_v0_8.py)

The public-release version changes the original environment-specific output path
to a repository-relative path.

Simulation logic is otherwise preserved for audit purposes.

Additional information:

[simulation/README.md](simulation/README.md)

### H-005 Results and Audit Artifacts

The H-005 evidence directory contains:

- raw v0.7 results;
- a public retrospective summary of the rejected v0.7 result;
- raw v0.8 results;
- a retrospective v0.8 audit summary;
- historical sensitivity analysis;
- links back to the published v0.8 engine.

[Browse H-005 evidence](experiments/h005-v07-v08/README.md)

### Historical v0.7 Source Status

The original historical `enterprise_sim_engine_v0_7.py` source has not yet been
recovered from the original working environment.

It will **not** be reconstructed and presented as the historical source.

When the original file is recovered, it will be added to the repository as an
audit artifact.

The absence of that historical source is therefore an explicit limitation of
the current repository.

---

## Scope and Limitations

The current simulation is a synthetic organizational model.

It is **not an empirically calibrated model of a specific company, workforce, or
AI system**.

Numeric parameters are used to test experimental mechanics and behavioral
hypotheses. They should not be interpreted as measured real-world effect sizes.

The currently published engines are rule-based stochastic simulations.

They do not yet invoke production LLM agents.

Future integration of production models will introduce additional sources of
variance, nondeterminism, model-version drift, provider behavior, prompt
sensitivity, and cost that will require their own experimental controls.

The project therefore distinguishes among:

**Current executed evidence**  
Rule-based organizational simulation and adversarial experimental auditing.

**Current prospective work**  
H-006 and continued development of stronger experimental integrity controls.

**Future research direction**  
Configurable heterogeneous LLM-powered organizational agents and direct
measurement of model × role × team × organizational interactions.

---

## Why Preserve Rejected Work?

A rejected result is useful evidence about the evaluation process.

Removing failed experiments would make the repository look cleaner while making
it less useful for understanding how conclusions were reached.

For that reason, rejected results, invalid metrics, corrected designs, and
retrospective explanations are preserved when practical.

The intent is to make the history of the experiment inspectable rather than
present only the final surviving claim.

---

## For Reviewers

If you have approximately **2 minutes**:

1. Read this README.
2. Read [REVIEW_GUIDE.md](REVIEW_GUIDE.md).

If you have approximately **5 minutes**:

1. Read the
   [false-positive audit case study](case-study/false-positive-audit.md).
2. Review the evidence-status distinction above.

If you want to inspect the implementation and raw evidence:

1. Review the
   [v0.8 engine](simulation/enterprise_sim_engine_v0_8.py).
2. Browse the
   [H-005 experiment artifacts](experiments/h005-v07-v08/README.md).
3. Review the
   [H-006 prospective design](prospective-research/H006/README.md).

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

## Guiding Idea

The project is not intended to tell researchers or practitioners what conclusions
they should draw.

Its goal is to make the experimental conditions, assumptions, observations,
limitations, and audit history sufficiently clear that others can examine the
evidence and draw their own conclusions.

If this work is successful, its most valuable future use may be something the
original project never anticipated.
