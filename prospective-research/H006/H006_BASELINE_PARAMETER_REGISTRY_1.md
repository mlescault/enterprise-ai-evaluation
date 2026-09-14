# PARAMETER & SENSITIVITY REGISTRY: MODULE H-006

**Identifier:** H006_BASELINE_PARAMETER_REGISTRY_1
**Status:** Draft — parameters unset, classification honest
**Governs:** H006_SPEC_FREEZE_1 (architecture/treatment boundaries unchanged by this document)

## How this registry classifies a parameter's basis

Four classes only, and every parameter below gets exactly one, stated plainly rather than dressed up:

- **empirical** — measured from real data this project actually has. (Nothing in this registry currently qualifies. If that changes, the source gets cited inline, not just asserted.)
- **historically informed practitioner prior** — a directional expectation from the framework author's own professional experience, stated by him, not inferred or assumed on his behalf. Used only where he's actually said so; never applied silently just because a parameter *sounds* like something a production background would know.
- **assumed / synthetic** — a placeholder chosen so the engine is executable, with no evidentiary claim behind it beyond "this seemed like a reasonable number to start from." This is the default class for almost everything below.
- **TBD** — not yet even a placeholder. Needs a value before baseline execution but none is proposed here.

The previous draft (the "Repository File Template" at the end of the H-006 handoff) mislabeled several assumed/synthetic numbers as if they had an empirical basis (e.g. citing "core technical engine onboarding profiles" for a 2-sprint ramp duration with no actual data behind it) and asserted one causal claim the model doesn't yet support (ramp duration affecting donor-pod slippage, when ramp duration governs *recipient-side* capacity realization and donor loss is a separate, not-yet-defined term). Both are corrected below by construction: every "Expected directional effect" line states only what the stated formula/schema actually implies, nothing upstream or downstream of it.

Two structural gaps turned up while building this — not changes to the frozen treatment boundaries, just terms the spec names but doesn't yet define a computation for. Flagged inline where they occur rather than silently resolved.

---

## 1. Capacity Physics Parameters

### 1.1 Ramp-up (recipient-side)

```
Parameter: BASE_RAMP_DURATION_SPRINTS
Class: capacity_physics
Baseline: TBD
Units: sprints
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale:
  Represents elapsed time before a transferred EngineerUnit reaches
  steady-state domain-adjusted productivity in its NEW (recipient) pod.

Expected directional effect:
  Holding other parameters constant, longer ramp duration delays
  realization of the recipient pod's Effective Incoming capacity term.
  It has no defined effect on the donor pod -- donor-side loss is
  governed separately by TRANSFER_OUT_LOSS_MODEL (1.3 below), not by
  how fast the recipient ramps.

Sensitivity required: Yes
Calibration status: Uncalibrated
```

```
Parameter: RAMP_CURVE_SHAPE
Class: capacity_physics
Baseline: TBD (candidates: linear, exponential-approach, step-function)
Units: n/a (functional form)
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale:
  The frozen spec (Layer 3) states ramp_factor "scales over time based
  on domain_familiarity" but does not specify the shape of that curve.
  This is a real gap, not a restatement of BASE_RAMP_DURATION_SPRINTS --
  duration says HOW LONG, this says HOW the unit's productivity moves
  from low to steady-state across that duration (e.g. a straight line
  vs. slow-then-fast vs. an immediate partial jump then a slow tail).

Expected directional effect:
  Not asserted. Different shapes with the same BASE_RAMP_DURATION_SPRINTS
  produce different early-sprint capacity even with identical final
  capacity -- this needs to be picked before the model is executable,
  not inferred from the duration parameter alone.

Sensitivity required: Yes (shape, not just duration)
Calibration status: Uncalibrated -- open decision, not yet a placeholder
```

### 1.2 Mentoring tax (recipient-side)

```
Parameter: SENIOR_MENTOR_TIME_DECREMENT
Class: capacity_physics
Baseline: TBD
Units: fraction of a mentor's productivity per newcomer mentored
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale:
  Feeds the Mentor Capacity Loss formula (Section 3 of the frozen spec):
  sum(newcomer.mentor_requirement x assigned_mentor_productivity).
  OPEN QUESTION, not resolved here: is this meant as a single global
  constant applied uniformly, or as the default/baseline value that
  populates a new EngineerUnit's own mentor_requirement field (Layer 1),
  which the formula already treats as per-unit and possibly
  heterogeneous? The frozen spec has both a global-sounding parameter
  name and a per-unit schema field for what appears to be the same
  quantity. This needs a decision before the registry can be more than
  a placeholder for it.

Expected directional effect:
  Holding other parameters constant, a larger value reduces the host
  pod's available senior capacity while newcomers are ramping, with no
  stated effect on any other pod.

Sensitivity required: Yes
Calibration status: Uncalibrated
```

### 1.3 Transfer-out loss (donor-side) -- gap flagged

```
Parameter: TRANSFER_OUT_LOSS_MODEL
Class: capacity_physics
Baseline: TBD
Units: n/a (functional form + coefficient)
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale:
  "Transfer Out Loss" appears as a term in the Net Effective Capacity
  formula (Layer 2) but, unlike Mentoring Tax and Coordination Overhead,
  the frozen spec never defines how it's computed. Simplest assumed form
  pending a decision: the departing unit's own (base_productivity x
  allocation_fraction) is removed from Gross Internal at transfer_start_tick,
  with no additional donor-side disruption tax beyond that direct loss.
  A more realistic alternative -- a temporary backfill/disruption
  penalty on the REMAINING donor-pod members, similar in spirit to the
  recipient's mentoring tax -- is plausible but not yet specified, and
  choosing it is filling in the physics, not altering the treatment
  boundary, so it belongs here rather than back in the frozen document.

Expected directional effect:
  Not asserted beyond the direct loss described above until a decision
  is made on whether a disruption-tax variant applies.

Sensitivity required: Yes, once a functional form is chosen
Calibration status: Uncalibrated -- functional form itself still open
```

### 1.4 External/borrowing coordination tax

```
Parameter: ARCHITECTURAL_DISTANCE_TAX_MULT
Class: capacity_physics
Baseline: TBD
Units: dimensionless multiplier
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale:
  Scales Coordination Overhead for temporary/external borrowing,
  per "architectural distance metrics" (Section 3 of the frozen spec).

Expected directional effect:
  Holding architectural distance constant, a larger multiplier increases
  the coordination-overhead deduction from that borrowed unit's
  effective contribution. No claim about which specialty pairs are
  "far" or "near" -- see ARCHITECTURAL_DISTANCE_METRIC below, which is
  a separate, currently undefined input this parameter depends on.

Sensitivity required: Yes
Calibration status: Uncalibrated
```

```
Parameter: ARCHITECTURAL_DISTANCE_METRIC
Class: capacity_physics
Baseline: TBD
Units: n/a (a distance value or lookup per specialty/pod pair)
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale:
  "Architectural distance" is named in the frozen spec's Coordination
  Overhead description but nothing defines what it measures between --
  specialty pairs (rendering/core_engine/tools), specific pods, or
  something else. Simplest assumed form pending a decision: a fixed
  3x3 specialty-adjacency table (same specialty = 0, adjacent
  specialties = 1, distant = 2), fed into ARCHITECTURAL_DISTANCE_TAX_MULT
  linearly. Not adopted here, just named as the minimal candidate.

Expected directional effect:
  Not asserted -- this is a missing input definition, not yet a
  parameter with a direction.

Sensitivity required: Yes, once defined
Calibration status: Uncalibrated -- definition itself still open
```

---

## 2. Environment & Initialization Parameters

```
Parameter: POD_SIZE_MATRIX
Class: environment_init
Baseline: TBD
Units: EngineerUnit count per pod
Permitted range: TBD (backlog's earlier EngineerPool sketch suggested
  6-12 units/pod as a starting granularity, not adopted here as a
  baseline, only noted as a prior candidate range)
Basis: assumed/synthetic unless calibrated
Rationale: Starting roster size per pod; affects how much a single
  transfer moves the needle proportionally.
Expected directional effect: Not asserted -- this is an initial
  condition, not a mechanic with a direction.
Sensitivity required: Yes
Calibration status: Uncalibrated
```

```
Parameter: WORKLOAD_DISTRIBUTION_INDEX
Class: environment_init
Baseline: TBD
Units: starting effort_required stock, per pod domain
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale: Initial backlog size each pod starts the run carrying.
Expected directional effect: Not asserted -- initial condition.
Sensitivity required: Yes
Calibration status: Uncalibrated
```

```
Parameter: COMMITMENT_PRIORITY_WEIGHTS
Class: environment_init
Baseline: TBD
Units: integer scale (launch-critical vs. low-priority)
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale: Feeds Weighted Schedule Slippage (Section 4.3 of the frozen
  spec) and any_launch_critical_commitment_broken.
Expected directional effect: Not asserted -- a weighting scheme, not a
  mechanic.
Sensitivity required: Yes
Calibration status: Uncalibrated
```

```
Parameter: RELATIONSHIP_CAPITAL_BASELINE
Class: environment_init
Baseline: TBD
Units: Agent.relationships.trust distribution (uniform vs. randomized;
  range 0.0-1.0 per the existing state_schema)
Permitted range: TBD
Basis: assumed/synthetic unless calibrated
Rationale: Directly feeds falsification criterion 3
  (Informal-Governance Substitution) -- how this is initialized
  determines how much room that alternative has to explain any
  observed effect, so it deserves at least as much care as the
  primary-estimand parameters, not a default afterthought.
Expected directional effect: Not asserted -- initial condition, though
  note it is the one parameter here that directly interacts with a
  falsification criterion rather than only with the primary mechanism.
Sensitivity required: Yes
Calibration status: Uncalibrated
```

---

## 3. Institutional Governance Properties (Treatments -- not calibrated parameters)

These are fixed by the frozen spec as the experimental manipulation itself, not estimated quantities, so they don't get a basis classification the way the physics parameters above do:

```
Vacuum Cell:  {"peer_rank_access": false, "tier3_escalation_access": false, "tier4_review_access": false, "mandate_challenge_access": false}
Parity Cell:  {"peer_rank_access": true,  "tier3_escalation_access": true,  "tier4_review_access": true,  "mandate_challenge_access": true}
```

Note for later, not a baseline-execution blocker: these two cells only test the all-or-nothing endpoints. A future factorial over individual affordances (e.g. `tier3_escalation_access=true` alone) could separate which specific piece of standing matters -- worth remembering as a follow-on, not something to add now under a frozen spec that explicitly prohibits changing the treatment structure pre-baseline.

---

## 4. Experimental Scale -- not in the frozen spec, still needed before execution

```
N_SEEDS_PER_CELL: TBD
K_PIS: TBD
```

Deliberately not filled with a round number carried over from H-005 (N=400, K=12). H-005-T's whole lesson was that N=30-50 could only ever detect implausibly large effects, and the number that worked (400) was sized against H-005's own observed base rates after several runs, not chosen up front. H-006's primary estimand (Impact Disposition Fraction, a fraction-of-signals metric) has a different statistical shape than a rare binary catastrophe event -- it may not need anywhere near 400 seeds/cell to be well-powered, or it may need more, depending on how many `GovernanceSignal`s a typical run even generates. Right sizing this needs a quick pilot run once the minimal slice exists, not a guess copied from a different estimand.

---

## Summary: what's actually decided vs. still open

Nothing numeric is decided. What's decided is the classification discipline itself, the correction to the ramp-duration directional claim, and two real gaps in the frozen spec's own physics (Transfer Out Loss and Architectural Distance have no defined computation yet, and the ramp curve's shape is separate from its duration). Those three belong to whoever fills in the minimal executable slice next -- they're modeling decisions, not treatment-boundary changes, so nothing here requires reopening H006_SPEC_FREEZE_1.
