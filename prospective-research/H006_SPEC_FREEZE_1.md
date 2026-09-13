# EXPERIMENTAL SPECIFICATION & PRE-REGISTRATION

## Module H-006: Capacity-Orchestration Consequence Governance

**Identifier:** `H006_SPEC_FREEZE_1`
**Status:** Frozen — Architecture Locked
**Methodological Standard:** Invariant Physics Layer / Structural Institutional Affordances Treatment

**Framing note (added when this was filed to the project, not part of the frozen content):** This tests a refinement of the H-006 idea first sketched in `backlog_deferred_design_post_v0_8.md`. The backlog sketch had Program *initiating* a reallocation request that leadership approves. This spec is the reverse and, on review, the stronger version: Engineering initiates the `SourcingAction` for its own reasons; Program only assesses the schedule fallout and emits a `GovernanceSignal`; the experiment is whether institutional standing determines whether that signal gets acted on or ignored. That's a more direct extension of H-005's own authority-vacuum framing (reacting to consequences you didn't create and can't control) than the original sketch was. The backlog entry should be read as superseded by this document for H-006's actual scope.

Baseline numeric parameters are tracked separately in `H006_BASELINE_PARAMETER_REGISTRY_1.md` — that document is explicitly NOT frozen and is still in draft (everything in it is `TBD` pending a minimal executable slice and, where relevant, the author's own practitioner priors). Nothing below constrains parameter values; it constrains structure, treatment boundaries, and estimands.

---

## 1. The Matched-Treatment Experimental Design Constraint

To support clean causal identification of the governance treatment within the simulation, all comparative runs between the Vacuum Cell and the Control/Parity Cells must utilize a strictly matched-treatment initial design.

For the first causal pass of H-006, the initial conditions up to the first governance checkpoint are deterministic mirror images:

- **Identical Stressor Environment:** The exact same random seed, task workload, environmental stressors, and dependency graph are injected across parallel cells.
- **Identical Sourcing Decision:** The engine forces an identical baseline capacity stressor and an identical initial `SourcingAction` from Engineering leadership.
- **The Treatment Boundary:** The system state, capacity physics, and Program's mathematical schedule assessments remain completely identical across cells. The simulation is only permitted to diverge after the initial `GovernanceSignal` is generated and agents interact with their cell-specific institutional affordances.

## 2. State Schema & Layered Architecture

### Layer 1: EngineerUnit (State Object)

```json
{
  "id": "string, unique",
  "home_pod_id": "ref: Pod",
  "current_pod_id": "ref: Pod",
  "specialty": "enum: rendering | core_engine | tools",
  "experience_level": "enum: junior | mid | senior",
  "base_productivity": "numeric",
  "domain_familiarity": "map: pod_id -> numeric (0.0 to 1.0)",
  "allocation_fraction": "numeric (0.0 to 1.0)",
  "transfer_state": "enum: stable | in_transit | ramping",
  "transfer_start_tick": "int | null",
  "ramp_progress": "numeric",
  "mentor_requirement": "numeric"
}
```

### Layer 2: PodCapacityState (Decomposed Velocity Tracking)

Net effective capacity represents an ongoing temporal rate, calculated invariant across all experimental cells:

Net Effective Capacity = Gross Internal + Effective Incoming + Effective External − Transfer Out Loss − Mentoring Tax − Coordination Tax

### Layer 3: SourcingAction (Separating Forecast from Realization)

To ensure Engineering is modeled as a rational actor working with bounded forecasts rather than reckless intent, their subjective expectations are decoupled from objective engine truth.

```json
{
  "id": "string, unique",
  "action_type": "enum: inter_pod_transfer | external_borrow | hire | vendor",
  "initiating_agent": "ref: Agent (EM | VP_Eng)",
  "source_pod": "ref: Pod | null",
  "target_pod": "ref: Pod",
  "engineer_units": "list of ref: EngineerUnit",
  "start_tick": "int",
  "expected_duration": "int",
  "engineering_rationale": "string",
  "engineering_expected_capacity_gain": "numeric",
  "engineering_expected_transition_cost": "numeric",
  "realized_state": {
    "realized_capacity_gain": "numeric",
    "realized_transfer_loss": "numeric",
    "realized_ramp_loss": "numeric",
    "realized_mentoring_tax": "numeric",
    "realized_coordination_tax": "numeric"
  },
  "status": "enum: logged | active | completed"
}
```

### Layer 4: ProgramScheduleAssessment & GovernanceSignal (Strict Observers)

Program acts strictly as an objective calculator. The `GovernanceSignal` is generated identically across all cells, with no structural modifiers affecting transmission velocity or receipt metrics.

Projected Duration = ceil(Effort Remaining / Net Effective Capacity)

- **Commitment Rule:** If Projected Completion > Commitment.deadline, status = at_risk. If current_tick > deadline and delivered = false, status = broken.

### Layer 5: Institutional Affordances (The Explicit Treatment Variables)

To prevent hidden parameter bias from dictating the conclusion, the experimental condition handles treatments as explicit institutional boolean facts rather than arbitrary numeric multipliers.

```json
{
  "peer_rank_access": "bool",
  "tier3_escalation_access": "bool",
  "tier4_review_access": "bool",
  "mandate_challenge_access": "bool"
}
```

### Layer 6: OperationalIntervention (The Executive Action Layer)

Tracks whether organizational leadership explicitly recognized and dispositioned the cost of the change, separating informed trade-offs from blind systemic breakdown.

```json
{
  "id": "string, unique",
  "trigger_signal": "ref: GovernanceSignal",
  "initiating_agent": "ref: Agent",
  "action_type": "enum: reverse_transfer | partial_restore | scope_cut | deadline_extension | reprioritize | accept_risk | no_action_explicit | no_response",
  "affected_pods": "list of ref: Pod",
  "affected_commitments": "list of ref: Commitment",
  "capacity_effect": "numeric",
  "scope_effect": "numeric",
  "schedule_effect": "numeric",
  "explicit_tradeoff_recorded": "bool",
  "executed_tick": "int | null"
}
```

- **Disposition Gating:** If `action_type` resolves to any value other than `no_response`, the system flags the signal as explicitly processed. An assignment of `no_response` denotes an impact that remained organizationally undispositioned within the observation window.

## 3. Temporal Capacity Physics (Invariants)

- **Dynamic Ramp-Up:** Incoming units start with a low `ramp_factor` that scales over time based on `domain_familiarity`.
- **Mentoring Tax:** Deducts productivity directly from the host pod's existing senior capacity pool: Mentor Capacity Loss = sum(Newcomer Mentor Requirement × Assigned Mentor Productivity).
- **Coordination Overhead:** Extracted from temporary studio/external borrowing based on architectural distance metrics, rather than a fixed efficiency constant.

## 4. Mathematical Estimands & System Metrics

### 4.1 Manipulation & Invariance Checks (Pre-Boundary Verification)

- **Forecast Error:** Verifies structural identity between subjective engineering expectation and objective engine realization: Forecast Error = Realized Net Capacity Change − Engineering Expected Net Capacity Change.
- **Net Portfolio Capacity Delta:** Verifies global identical capacity behavior across paired runs: Net Portfolio Delta = Recipient Gain − Donor Loss − Transition Taxes.

### 4.2 Primary H-006 Estimands (Post-Boundary Governance Metrics)

- **Impact Disposition Fraction:** Measures structural information processing efficiency: Impact Disposition Fraction = (Program-identified impacts with action_type ≠ no_response) / (Total Program-identified impacts).
- **Warning-to-Disposition Latency:** Evaluates temporal lag between signal creation and explicit disposition. Unresolved signals at cycle close are marked as right-censored metrics (`intervention_tick = null`), enabling clean survival analysis.

### 4.3 Secondary Consequences (Downstream Delivery Outcomes)

- **Weighted Schedule Slippage:** Captures prioritization impacts over raw velocity sums: Weighted Slippage = sum_i(Slippage_i × CommitmentPriority_i).
- `broken_commitment_count` (Integer)
- `broken_commitment_fraction` (Ratio)
- `any_launch_critical_commitment_broken` (Boolean)

## 5. Falsification Criteria & Alternative Outcomes

1. **The Structural Null:** If the Vacuum Cell and the Parity Cell receive identical `GovernanceSignals` and exhibit statistically indistinguishable warning-to-disposition latency and impact-disposition rates, H-006's primary governance hypothesis is not supported. Variance in downstream schedule slippage or commitment preservation represents separate delivery outcomes.
2. **Portfolio Optimization Alternative:** If Engineering's local sourcing action generates localized schedule damage but successfully yields a net-positive increase in global portfolio delivery efficiency, while `explicit_tradeoff_recorded` maps directly to intentional risk acceptance, the results represent a rational portfolio trade-off rather than a governance failure.
3. **Informal-Governance Substitution:** If high relationship trust (`Agent.relationships.trust`) between the PM and Engineering leadership substantially attenuates or eliminates the variance associated with formal Program standing, the results support informal-governance substitution under the tested conditions.

## 6. Pre-Run Integrity Gate

Prior to the application of the treatment boundary, paired Vacuum/Parity simulation runs must remain entirely state-identical. The structural framework is fully locked down and explicitly designed to detect and prevent treatment leakage or affirmative-result bias. The pre-boundary runtime must match perfectly across:

- Stressor injection arrays and seed-generated task states.
- Engineering `SourcingAction` parameters and target profiles.
- Objective realized capacity physics (`PodCapacityState`).
- Evaluated metrics for Forecast Error and Net Portfolio Capacity Delta.
- Generated `ProgramScheduleAssessment` and downstream `GovernanceSignal` content.

**Enforcement:** Any observed pre-boundary state divergence or calculation asymmetry immediately invalidates the paired run as an engine-level implementation failure.

**Note carried from the review discussion, not part of the original freeze text:** this gate protects against a bug type this project hasn't actually hit yet (pre-boundary divergence). The bug types that have actually hit this project (v0.6's bid constants, v0.7's backlog conflation) were post-boundary miscoding of which outcomes belong to which pathway. This gate is necessary but not sufficient — the minimal executable slice needs the same post-boundary scrutiny H-005 eventually got, not just this pre-boundary check.

## Permitted Operational Scope Following Freeze

```
[H006_SPEC_FREEZE_1 STAMP REGISTERED]
```

**Permitted Modifications:**

- Code-level bug fixes required to make the execution engine strictly conform to these architectural specifications.
- Parameter value binding defined entirely in `H006_BASELINE_PARAMETER_REGISTRY_1`.
- Pre-registered range updates for standard sensitivity loops.
- Non-functional syntax or markdown formatting documentation updates.

**Strictly Prohibited Modifications Prior to Baseline Execution:**

- Structural shifts to the treatment boundaries or calculation sequence.
- Alterations to primary/secondary estimands or evaluation rules.
- Modifications to institutional affordance properties or structural boolean switches based on early observed test-cell behavior.

---

**Status as of Sept 12 2026:** Frozen through the stamp above. No baseline execution yet — no minimal executable slice has been built or run. Recommended before further freezing of anything downstream (per review discussion): build the smallest possible executable slice (EngineerUnit + PodCapacityState + one SourcingAction type + Institutional Affordances only, with ramp/mentoring/distance taxes stubbed to flat constants) and run it before investing further in unexecuted architecture — this project's actual working method has been spec-then-bug-then-fix-then-repeat, not spec-frozen-before-first-run.
