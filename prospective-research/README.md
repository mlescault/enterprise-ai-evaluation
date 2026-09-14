# H-006: Capacity-Orchestration Consequence Governance

[← Back to repository overview](../../README.md)

## Status

**Prospective design / preregistration in progress. Baseline not yet executed.**

H-006 is the next planned experiment in the organizational simulation.

Its purpose is to study the consequences of capacity-orchestration decisions while applying lessons learned from the H-005 audit sequence before experimental results are produced.

The architecture and integrity-gate direction are defined. Baseline execution remains blocked until unresolved parameters and the statistical plan are complete.

H-006 should therefore be interpreted as evidence of **prospective experimental-design discipline**, not as an executed experiment or empirical finding.

---

## Why H-006 Exists

H-005 exposed two different ways an apparently strong experimental result could be structurally misleading:

1. treatment leakage created unequal outcome pathways between conditions;
2. a later comparative metric was found to be structurally unavailable to the control condition.

H-006 moves more of that scrutiny upstream.

Rather than relying primarily on post-result auditing, the design introduces explicit parameter registration, treatment-boundary checks, pre-execution invariants, and execution gates intended to detect structural asymmetries before baseline runs occur.

---

## Documents

- [Frozen experimental specification](https://github.com/mlescault/enterprise-ai-evaluation/blob/main/prospective-research/H006/H006_SPEC_FREEZE_1.md)
- [Baseline parameter registry](https://github.com/mlescault/enterprise-ai-evaluation/blob/main/prospective-research/H006/H006_BASELINE_PARAMETER_REGISTRY_1.md)

These documents describe the current prospective design state.

---

## Current Execution Gate

Baseline execution is intentionally blocked.

Before H-006 can run, remaining TBD fields in the parameter registry must be resolved and the statistical plan must be completed.

The current registry includes unresolved items such as environment parameters, initialization details, workload assumptions, observation definitions, and other values that could materially affect experimental behavior.

A TBD that affects baseline interpretation is treated as a blocker rather than filled in after results are visible.

---

## Experimental Integrity Direction

The H-006 design is intended to include stronger pre-execution controls such as:

- explicit treatment definitions;
- registered parameter values;
- paired-condition initialization controls;
- pre-treatment equivalence checks;
- treatment-boundary invariants;
- explicit outcome definitions;
- documented assumptions and synthetic parameters;
- execution blocking when required fields remain unresolved.

The objective is not to guarantee that future experiments contain no flaws.

The objective is to make important assumptions visible earlier and reduce the opportunity for treatment or measurement asymmetries to survive until after results are produced.

---

## Evidence Status

**Executed:** No.

**Baseline run:** Not yet performed.

**Statistical results:** None.

**Architecture / integrity-gate design:** Defined.

**Parameter registry:** In progress; unresolved fields remain.

**Statistical plan:** Not yet complete.

**Interpretive status:** Prospective methodology only.

---

## Relationship to H-005

H-005 demonstrated the value of auditing a result after it strongly confirmed a practitioner hypothesis.

H-006 represents the next methodological step: move as much of that skepticism as practical to the period **before** execution.

The intended progression is:

**H-005:** execute → observe → audit → discover structural problems → reject invalid findings.

**H-006:** specify → register → verify treatment boundaries → satisfy integrity gates → execute.

Whether H-006 ultimately produces an interesting result is secondary to whether the experimental structure makes that result trustworthy.

---

## Scope

H-006 remains part of the current **rule-based stochastic organizational simulation** work.

It does not currently involve production LLM agents.

The heterogeneous LLM-agent research direction is a later planned phase described in the repository [ROADMAP](../../ROADMAP.md).
