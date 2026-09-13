# Enterprise AI Evaluation

Adversarial evaluation and multi-agent simulation of enterprise software-production decision making, governance, and capacity allocation.

## Reviewer Guide

Short on time? See the [Reviewer Guide](REVIEW_GUIDE.md) for the fastest
path through the evidence.

## Overview

This repository contains a set of experiments and evaluation artifacts exploring how AI systems reason about complex enterprise software organizations.

The work draws on real-world technical program leadership experience and focuses on problems such as:

- engineering capacity and staffing decisions
- cross-team dependencies
- delivery risk and milestone pressure
- organizational governance and escalation
- multi-agent decision making under incomplete information
- adversarial auditing of AI evaluation methods

## Evaluation Philosophy

The objective is not to build simulations that reproduce a predetermined management philosophy.

Experiments are structured so that the modeled system can support, contradict, or refine the practitioner's initial hypothesis.

Particular emphasis is placed on:

- explicit assumptions
- falsifiable hypotheses
- treatment isolation
- adversarial review
- reproducibility
- bounded conclusions

## Current Work

### Organizational Simulation Audit

[Read the full false-positive audit case study](case-study/false-positive-audit.md)

An early multi-agent experiment produced a strong result supporting the original practitioner hypothesis.

A subsequent audit identified condition-specific treatment leakage in the simulation engine. The result was rejected rather than reported.

After correcting the implementation and rerunning the experiment, a second audit identified a subtler measurement issue in one of the replacement outcome metrics. That metric was also retired.

The surviving result concerns differences in ambiguity-resolution behavior rather than differences in underlying agent competence.

Supporting code, results, and the full audit trail will be added to this repository.

### H-006: Capacity-Orchestration Consequence Governance

H-006 is a prospective experiment examining how institutional governance affects the consequences of engineering-capacity allocation decisions.

The experimental design and parameter registry are being frozen before baseline execution so that modeling assumptions cannot be adjusted in response to observed results.

**Status: design/pre-registration phase — baseline not yet executed.**

## Repository Status

This repository is currently being assembled as a public AI-evaluation work sample. Additional simulation code, experimental results, evaluation rubrics, and documentation are being added incrementally.
