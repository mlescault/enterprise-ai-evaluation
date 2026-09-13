# Case Study: Identifying and Correcting a False Positive

## Purpose

This case study documents the adversarial audit of a multi-agent
organizational simulation designed to explore enterprise
software-engineering governance.

The objective was not to demonstrate that a particular management
philosophy was correct. The experiment was designed so that the
simulation could support, contradict, or refine the practitioner's
initial hypothesis.

## Experimental Question

The simulation examined whether a structural authority vacuum in a
software organization changes how unresolved cross-team ambiguity is
handled over repeated execution cycles.

The experiment used a factorial design involving:

- structural rank parity versus a structural rank gap
- access versus lack of access to formal organizational mandate

The combination of a structural rank gap and no mandate access
represented the "Vacuum" condition.

## The Initial Result

Engine v0.7 produced a large separation between experimental
conditions.

The result strongly supported the original practitioner hypothesis.

That agreement triggered additional scrutiny rather than acceptance.

## Discovery of the False Positive

A code-level audit found that the simulation contained
condition-specific treatment leakage.

Certain forms of rework could enter a permanent-backlog pathway only
under particular treatment conditions. This meant that eligibility for
the measured outcome was inadvertently coupled to the treatment itself.

The observed separation therefore could not be interpreted as evidence
for the hypothesis.

**The result was rejected.**

## Engine v0.8

The simulation was revised to separate the organizational treatment
from the physical degradation and backlog mechanisms.

The corrected experiment was rerun at:

- N = 400 seeds per cell
- 12 Program Increment cycles per seed

The revised simulation produced a narrower behavioral result.

Baseline miss rates remained approximately equal across conditions.
The important difference was how agents responded after ambiguity
appeared.

Agents operating in the Vacuum condition were substantially more
likely to resolve ambiguity by guessing, while agents with access to
formal institutional mechanisms were substantially more likely to
force explicit resolution.

The surviving conclusion was therefore about **ambiguity-resolution
behavior**, not agent competence.

## Auditing the Fix

The v0.8 audit uncovered another problem.

A headline "catastrophe" metric initially appeared to show substantial
separation between conditions. Further inspection showed that the
control condition was structurally unable to enter the pathway being
counted.

The control result was therefore not evidence of superior performance;
the outcome simply was not reachable under the same measurement path.

That metric was retired rather than reported as a finding.

## Redesign

The successor outcome design requires every experimental condition to
share the same consequence pathway:

miss → escalate or guess → correct or wrong → caught or latent

Experimental treatments may change the probability of each transition,
but may not change whether an outcome is eligible to occur or be
measured.

A pre-treatment integrity gate is also required before aggregate
results are accepted.

## What I Took From the Exercise

Three evaluation principles emerged from this work:

1. **Audit results that agree strongly with prior beliefs.**
   Confirmation is a reason for additional scrutiny, not reduced
   scrutiny.

2. **Separate treatment, mechanism, and outcome.**
   Experimental conditions may influence behavior without defining
   which outcomes are measurable.

3. **Audit the correction as aggressively as the original defect.**
   Removing one source of leakage can introduce another.

The goal of evaluation is not to produce an impressive result.

The goal is to determine which results survive attempts to disprove
them.

## Status

- Engine v0.7 result: rejected
- Engine v0.8 behavioral finding: retained with bounded interpretation
- v0.8 catastrophe metric: rejected
- successor consequence metric: specified, not yet executed
