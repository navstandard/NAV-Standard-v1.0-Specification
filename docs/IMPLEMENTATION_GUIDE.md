# Implementation Guide

Non-normative orientation for implementers.

## Reading Order

Start with `specification/S1_CHARTER.md` for purpose and boundaries. Read `specification/VERDICT_TAXONOMY.md` for semantic ownership. Read `specification/SPEC.md` for the NAV Certificate Format v1 representation and validation requirements. Read `specification/GOVERNANCE.md` for maintenance and change process.

## Certificate Structure

`specification/SPEC.md` defines the v1 certificate object, including evaluated output identity, authority snapshot identity, assertion records, decision, and integrity hash.

## Integrity Workflow

Use `specification/SPEC.md` section "Canonical Serialization and Integrity Hash" as the controlling source. A validator removes `integrity_sha256`, serializes the remaining certificate body canonically, computes SHA-256, and compares the result to the recorded hash.

## Decision Recalculation

`specification/SPEC.md` describes decision recomputation as an optional internal-consistency check. It does not establish authenticity or factual correctness.

## Distinctions

Integrity means the certificate body matches the recorded hash. Internal consistency means recorded fields agree under the v1 rules. Authenticity requires issuer authentication, which NAV Certificate Format v1 does not provide. Factual correctness is not established merely by certificate integrity.
