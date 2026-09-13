# PUBLICATION NOTE
#
# This is the v0.8 engine used in the documented H-005 audit sequence.
# The catastrophe metric implemented in this historical version was
# subsequently determined to be structurally invalid and is not reported
# as a retained finding.
#
# See: ../case-study/false-positive-audit.md
#
# Public-release change:
# - The output file path was changed from an environment-specific absolute
#   path to a repository-relative path.
# - Simulation logic is otherwise unchanged.
#
# The original engine comments below are retained as contemporaneous
# documentation of what was believed at the time of execution.

"""
Enterprise Multi-Agent Program Management Simulation -- Engine v0.8
==============================================================================

The properly-scoped vacant-seat pass Grok's fork called for, and the last
planned iteration on the catastrophic-tail formulation of H-005 before that
line gets frozen (H-005-R) or shelved regardless of what this run shows.

WHAT'S DIFFERENT FROM v0.7 (the bug this fixes)
------------------------------------------------
v0.7 routed every UNCONTESTED-MANDATE-WRONG outcome into a backlog pool that
never pays down, modeling it as "permanently unreviewable." That conflated
"uncontested" (true of every mandate assertion, by spec design) with
"unreviewable" (specifically: a genuinely, structurally vacant seat with no
principal who could ever revisit the call). Since only the mandate-holding
condition (parity) could ever produce that outcome, the 13x gap it produced
was an artifact of which condition happened to hold the one pathway wired to
never heal -- not a finding about rank gaps or authority.

v0.8's fix grounds "unreviewable" in the hypothesis's OWN definition instead
of in engine plumbing:

    principal_seat_vacant = structural_rank_gap AND pm_mandate_access == "none"

That is exactly H-005's own definition of the vacuum condition: "a function
with coordination accountability but no mandate/veto power and a standing
rank gap." A cell only satisfies this when BOTH conditions hold -- gap=True
with mandate=full_capped does NOT count (mandate access is itself a form of
standing), and gap=False does NOT count regardless of mandate (no gap means
an ordinary peer relationship exists). This is a deliberate, named
consequence of the hypothesis's own definition, not an accidental coupling
to whichever pathway happens to fire -- but it's disclosed as exactly that:
by construction, only ONE of the four factorial cells can ever generate
unreviewable backlog. The open empirical questions are (a) how much backlog
actually accumulates there given realistic guess/miss rates, and (b) whether
that's enough to cross the catastrophe threshold -- not whether the pathway
exists, which is true by definition.

Mechanically: under principal_seat_vacant, Program has no mandate to assert
(mandate=none by definition of the cell) and can still WIN negotiations
(that's a real institutional channel -- contested, reviewable). Only a bare
GUESS -- attempted-and-failed escalation, or no attempt at all -- that turns
out wrong has no one with standing behind it, and that specific pathway's
backlog is what does not pay down. Forced-and-wrong via a WON negotiation
remains tracked but not catastrophe-eligible in every cell (decision_model's
good-decision/bad-outcome quadrant, unchanged since v0.6b). Forced-and-wrong
via mandate (only possible in the two mandate=full_capped cells, neither of
which is ever vacant) goes to the ordinary reviewable/paydown-eligible pool,
consistent with the spec's own platform_investment_reversal_example.

SCOPE OF THIS RUN
------------------
Full 2x2 factorial (structural_rank_gap x pm_mandate_access), run at BOTH
scales named in Grok's fork:
  - K=1 PI:  replicates v0.6b's own finding (a single episode in one PI
    cannot clear a properly rare-event-scaled threshold) under the NEW
    vacant-seat logic, as a robustness check -- expected to be near-zero
    everywhere, for the same arithmetic reason as before, not a failure to
    find something.
  - K=12 PIs (~6-week cadence): the real, pre-registered test, unchanged
    cadence/mixed-schedule/carry-over machinery from v0.7.

N_SEEDS bumped from v0.7's 50 to 400/cell, per the stat-power discussion:
at observed base rates near 0.02-0.05, N=30-50 can only ever detect
implausibly large (>5x) effects -- which is exactly the range every prior
"significant" result in this project turned out to be an artifact at. 400
gives reasonable power for a ~3x effect at these base rates and is still
computationally trivial (no LLM calls).

PRE-REGISTERED ESTIMANDS (decided before running, not after):
  PRIMARY:   hazard-by-PI curve (K=12 only) for all four cells, and
             unreviewable_backlog_share (mean per-seed share of final total
             backlog that is unreviewable) -- continuous metrics, not
             subject to the rare-binary-event power problem.
  SECONDARY / CONFIRMATORY: final cumulative catastrophe probability per
             cell with Wilson 95% CIs, and a two-proportion z-test between
             the two theoretically central cells (vacuum vs. parity) --
             reported honestly even though it is likely underpowered for
             anything smaller than a large effect; that limitation is
             stated up front, not discovered after the fact.

STILL PLACEHOLDER, FLAGGED: paydown_rate, belief-shift magnitudes, mixed-
schedule probabilities, mandate cap/PI, tenure bonus rate -- unchanged from
v0.7, none calibrated against anything real. The vacant-seat gating above is
new and is a modeling choice grounded in the spec's own hypothesis text, not
an empirical calibration either.
"""

import random
import json
import math
import statistics
from dataclasses import dataclass, field
from typing import Optional

POD_CAPACITY_PER_SPRINT = 100
N_SPRINTS = 6
FULL_PI_CAPACITY = N_SPRINTS * POD_CAPACITY_PER_SPRINT   # 600
N_SEEDS = 400

GUESS_EFFORT = POD_CAPACITY_PER_SPRINT * 0.3   # 30
CATASTROPHE_MIN_GAP_SPRINTS = 1
CATASTROPHE_MIN_CAPACITY_FRACTION = 0.15
REWORK_INVALIDATION_FRACTION = 1.0
TIER2_POOL_PER_PI = 6
PAYDOWN_RATE = 0.20
UNREVIEWABLE_PAYDOWN_RATE = 0.0   # by definition: a vacant seat is never revisited.
                                   # Sensitivity to relaxing this is checked separately,
                                   # not baked into the headline number as if it were free.
BELIEF_MISMATCH_THRESHOLD = 3
BELIEF_GUESS_PROB_BUMP = 0.20
BELIEF_ESCALATE_PROB_MULT = 0.70
TENURE_BONUS_PER_PI = 0.05
TENURE_BONUS_CAP = 1.0
MANDATE_USES_PER_PI = 1

PM_BID_RANGE = (1.0, 5.0)
PDM_DEFENSE_RANGE = (2.0, 4.0)
RANK_GAP_BID_DISCOUNT = 0.6

P_NO_AMBIGUITY_THIS_PI = 0.30
P_DISAGREEMENT_GIVEN_AMBIGUITY = 0.55


@dataclass
class Condition:
    name: str
    structural_rank_gap: bool
    pm_mandate_access: str   # "none" | "full_capped"

    @property
    def principal_seat_vacant(self) -> bool:
        # Grounded in H-005's own definition of the vacuum condition -- not
        # an engine-plumbing accident. True for exactly one of the four
        # factorial cells, by construction.
        return self.structural_rank_gap and self.pm_mandate_access == "none"


@dataclass
class PIEvent:
    has_event: bool
    internal_disagreement: bool = False
    signal_sprint: int = 99
    signal_correct: bool = True
    finalize_sprint: int = 1
    true_value: str = "B"
    signal_value: str = "B"


def draw_pi_event(rng: random.Random) -> PIEvent:
    if rng.random() < P_NO_AMBIGUITY_THIS_PI:
        return PIEvent(has_event=False, finalize_sprint=1)

    disagreement = rng.random() < P_DISAGREEMENT_GIVEN_AMBIGUITY
    true_value = "B"
    if disagreement:
        signal_sprint = rng.randint(3, 5)
        signal_correct = rng.random() < 0.5
        finalize_sprint = min(N_SPRINTS, rng.randint(signal_sprint + 1, N_SPRINTS + 1))
    else:
        signal_sprint = 1
        signal_correct = True
        finalize_sprint = rng.randint(2, 4)

    signal_value = true_value if signal_correct else ("A" if true_value == "B" else "B")
    return PIEvent(
        has_event=True, internal_disagreement=disagreement, signal_sprint=signal_sprint,
        signal_correct=signal_correct, finalize_sprint=finalize_sprint,
        true_value=true_value, signal_value=signal_value,
    )


@dataclass
class SeedTrace:
    reviewable_backlog: float = 0.0
    unreviewable_backlog: float = 0.0
    mismatch_count: int = 0
    belief_spawned: bool = False
    catastrophic: bool = False
    first_catastrophe_pi: Optional[int] = None
    backlog_by_pi: list = field(default_factory=list)
    unreviewable_share_by_pi: list = field(default_factory=list)
    guesses: int = 0
    forced: int = 0
    misses: int = 0


def decision_value(sprint: int, ev: PIEvent, rng: random.Random) -> str:
    if sprint < ev.signal_sprint:
        return rng.choice(["A", "B"])
    return ev.signal_value


def run_pi(condition: Condition, ev: PIEvent, trace: SeedTrace, pi_index: int, rng: random.Random):
    if not ev.has_event:
        return

    tier2_remaining = TIER2_POOL_PER_PI
    mandate_used = 0
    guessed = forced = False
    guess_sprint = guess_value = None
    forced_sprint = forced_via = forced_value = None
    finalized = False

    guess_prob_bonus = BELIEF_GUESS_PROB_BUMP if trace.belief_spawned else 0.0
    escalate_mult = BELIEF_ESCALATE_PROB_MULT if trace.belief_spawned else 1.0
    tenure_bonus = min(TENURE_BONUS_CAP, TENURE_BONUS_PER_PI * pi_index)

    for sprint in range(1, N_SPRINTS + 1):
        if finalized:
            break
        if sprint >= ev.finalize_sprint:
            finalized = True
            break

        if not guessed and not forced:
            escalate_prob = 0.35 * escalate_mult
            guess_prob = min(0.95, 0.15 + 0.15 * sprint + guess_prob_bonus)
            roll = rng.random()

            can_mandate = condition.pm_mandate_access == "full_capped" and mandate_used < MANDATE_USES_PER_PI
            if roll < escalate_prob and (tier2_remaining > 0 or can_mandate):
                if can_mandate:
                    success, cost, via = True, 0.0, "mandate"
                    mandate_used += 1
                else:
                    raw_bid = rng.uniform(*PM_BID_RANGE)
                    if tier2_remaining < raw_bid:
                        success, cost, via = False, 0.0, "negotiation"
                    else:
                        effective_bid = raw_bid * (RANK_GAP_BID_DISCOUNT if condition.structural_rank_gap else 1.0)
                        effective_bid += tenure_bonus
                        defense_bid = rng.uniform(*PDM_DEFENSE_RANGE)
                        success = effective_bid > defense_bid
                        cost = raw_bid
                    via = "negotiation"
                tier2_remaining -= cost
                if success:
                    forced, forced_sprint, forced_via = True, sprint, via
                    forced_value = decision_value(sprint, ev, rng)
                    finalized = True
                    break
            elif roll < escalate_prob + guess_prob:
                guessed, guess_sprint = True, sprint
                guess_value = decision_value(sprint, ev, rng)

    # --- score ---
    if forced:
        trace.forced += 1
        if forced_value != ev.true_value:
            trace.misses += 1
            trace.mismatch_count += 1
            invalidated = GUESS_EFFORT * REWORK_INVALIDATION_FRACTION
            if forced_via == "mandate":
                # Uncontested, but mandate access IS standing -- ordinary,
                # correctable pool (matches platform_investment_reversal_example).
                trace.reviewable_backlog += invalidated
                root_cause, gap = "uncontested_mandate_cut", 0
            else:
                # Won, contested negotiation and wrong: ordinary risk, not
                # catastrophe-eligible (decision_model's good-decision/
                # bad-outcome quadrant).
                trace.reviewable_backlog += invalidated
                root_cause, gap = None, None
            if root_cause is not None:
                total_backlog = trace.reviewable_backlog + trace.unreviewable_backlog
                if gap >= 0 and total_backlog >= CATASTROPHE_MIN_CAPACITY_FRACTION * FULL_PI_CAPACITY:
                    if not trace.catastrophic:
                        trace.catastrophic = True
                        trace.first_catastrophe_pi = pi_index

    elif guessed:
        trace.guesses += 1
        if guess_value != ev.true_value:
            trace.misses += 1
            trace.mismatch_count += 1
            invalidated = GUESS_EFFORT * REWORK_INVALIDATION_FRACTION
            if condition.principal_seat_vacant:
                trace.unreviewable_backlog += invalidated   # no paydown, ever
            else:
                trace.reviewable_backlog += invalidated
            gap = ev.finalize_sprint - guess_sprint
            total_backlog = trace.reviewable_backlog + trace.unreviewable_backlog
            if gap >= CATASTROPHE_MIN_GAP_SPRINTS and total_backlog >= CATASTROPHE_MIN_CAPACITY_FRACTION * FULL_PI_CAPACITY:
                if not trace.catastrophic:
                    trace.catastrophic = True
                    trace.first_catastrophe_pi = pi_index

    if trace.mismatch_count >= BELIEF_MISMATCH_THRESHOLD:
        trace.belief_spawned = True


def simulate_seed(condition: Condition, rng: random.Random, k_pis: int) -> SeedTrace:
    trace = SeedTrace()
    for pi_index in range(1, k_pis + 1):
        trace.reviewable_backlog *= (1 - PAYDOWN_RATE)
        trace.unreviewable_backlog *= (1 - UNREVIEWABLE_PAYDOWN_RATE)
        ev = draw_pi_event(rng)
        run_pi(condition, ev, trace, pi_index, rng)
        total = trace.reviewable_backlog + trace.unreviewable_backlog
        trace.backlog_by_pi.append(total)
        trace.unreviewable_share_by_pi.append(trace.unreviewable_backlog / total if total > 0 else 0.0)
    return trace


def wilson_ci(x: int, n: int, z: float = 1.96):
    if n == 0:
        return (0.0, 0.0)
    phat = x / n
    denom = 1 + z * z / n
    center = phat + z * z / (2 * n)
    margin = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return ((center - margin) / denom, (center + margin) / denom)


def two_prop_z_test(x1, n1, x2, n2):
    p1, p2 = x1 / n1, x2 / n2
    p_pool = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se == 0:
        return 0.0, 1.0
    z = (p1 - p2) / se
    p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return z, p_value


def run_cell(condition: Condition, n_seeds: int, base_seed: int, k_pis: int):
    traces = [simulate_seed(condition, random.Random(base_seed * 104729 + i), k_pis) for i in range(n_seeds)]
    n = len(traces)

    hazard_by_pi = []
    for k in range(1, k_pis + 1):
        occurred_by_k = sum(1 for t in traces if t.catastrophic and t.first_catastrophe_pi is not None and t.first_catastrophe_pi <= k)
        hazard_by_pi.append(occurred_by_k / n)

    mean_backlog_by_pi = [statistics.mean(t.backlog_by_pi[k] for t in traces) for k in range(k_pis)]
    mean_unrev_share_by_pi = [statistics.mean(t.unreviewable_share_by_pi[k] for t in traces) for k in range(k_pis)]

    n_cat = sum(1 for t in traces if t.catastrophic)
    ci_lo, ci_hi = wilson_ci(n_cat, n)

    return {
        "condition": condition.name,
        "structural_rank_gap": condition.structural_rank_gap,
        "pm_mandate_access": condition.pm_mandate_access,
        "principal_seat_vacant": condition.principal_seat_vacant,
        "n_seeds": n,
        "k_pis": k_pis,
        "catastrophe_count": n_cat,
        "final_cumulative_catastrophe_prob": hazard_by_pi[-1] if hazard_by_pi else 0.0,
        "catastrophe_prob_wilson_95ci": [round(ci_lo, 4), round(ci_hi, 4)],
        "hazard_by_pi": hazard_by_pi,
        "mean_backlog_by_pi": mean_backlog_by_pi,
        "mean_unreviewable_share_by_pi": mean_unrev_share_by_pi,
        "mean_final_backlog": statistics.mean(t.reviewable_backlog + t.unreviewable_backlog for t in traces),
        "mean_unreviewable_backlog_final": statistics.mean(t.unreviewable_backlog for t in traces),
        "mean_unreviewable_share_final": statistics.mean(t.unreviewable_share_by_pi[-1] for t in traces) if k_pis > 0 else 0.0,
        "belief_spawn_rate": sum(1 for t in traces if t.belief_spawned) / n,
        "mean_guesses_per_seed": statistics.mean(t.guesses for t in traces),
        "mean_forced_per_seed": statistics.mean(t.forced for t in traces),
        "mean_misses_per_seed": statistics.mean(t.misses for t in traces),
    }


def build_factorial():
    return [
        Condition(name="vacuum: gap=True x mandate=none", structural_rank_gap=True, pm_mandate_access="none"),
        Condition(name="gap=True x mandate=full_capped", structural_rank_gap=True, pm_mandate_access="full_capped"),
        Condition(name="gap=False x mandate=none", structural_rank_gap=False, pm_mandate_access="none"),
        Condition(name="parity: gap=False x mandate=full_capped", structural_rank_gap=False, pm_mandate_access="full_capped"),
    ]


if __name__ == "__main__":
    output = {"engine_version": "0.8", "n_seeds_per_cell": N_SEEDS}

    for k_pis, label in [(1, "k1"), (12, "k12")]:
        conditions = build_factorial()
        results = [run_cell(c, N_SEEDS, base_seed=(100 * k_pis + i + 1), k_pis=k_pis) for i, c in enumerate(conditions)]
        output[label] = {"k_pis": k_pis, "results": results}

        print(f"=== K={k_pis} PI(s), N={N_SEEDS}/cell ===\n")
        for r in results:
            print(r["condition"], f"(principal_seat_vacant={r['principal_seat_vacant']})")
            print("  final cumulative catastrophe prob:", round(r["final_cumulative_catastrophe_prob"], 4),
                  " 95% CI:", r["catastrophe_prob_wilson_95ci"])
            print("  mean final backlog:", round(r["mean_final_backlog"], 1),
                  " unreviewable:", round(r["mean_unreviewable_backlog_final"], 1),
                  " unrev share:", round(r["mean_unreviewable_share_final"], 3))
            print("  belief_spawn_rate:", round(r["belief_spawn_rate"], 3))
            print("  mean guesses/forced/misses:", round(r["mean_guesses_per_seed"], 2),
                  round(r["mean_forced_per_seed"], 2), round(r["mean_misses_per_seed"], 2))
            print()

        # Central comparison: vacuum vs parity
        vac = results[0]
        par = results[3]
        z, p = two_prop_z_test(vac["catastrophe_count"], vac["n_seeds"], par["catastrophe_count"], par["n_seeds"])
        print(f"  vacuum vs parity two-proportion z-test: z={z:.3f}, p={p:.4f}")
        print(f"  vacuum n_cat={vac['catastrophe_count']}/{vac['n_seeds']}, parity n_cat={par['catastrophe_count']}/{par['n_seeds']}")
        print()

        output[label]["vacuum_vs_parity_z"] = z
        output[label]["vacuum_vs_parity_p"] = p

    with open("h005_v0_8_results.json", "w") as f:
        json.dump(output, f, indent=2)
