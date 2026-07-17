# ARCHITECTURE_REGISTRY.md

NAV Standards Constitutional Registry

## Purpose

This registry identifies the authoritative governing artifacts of the NAV standard.

The NAV standards package is self-contained. Interpretation of NAV shall not depend on private VARI or Thirty Seven Inc. architectural documents.

Artifacts listed as governing define NAV doctrine within their stated scope. Frozen artifacts are not revised through ordinary engineering work. Changes to frozen doctrine require an explicit Architectural Amendment.

The company-wide relationship between VARI engineering artifacts is governed separately by GOVERNING_PRECEDENCE.md and does not alter the self-contained authority of this standards package.

---

## Status Definitions

Draft

An artifact under development with no governing authority.

Approved

An artifact accepted for use within its stated scope but not declared immutable.

Frozen

A governing artifact whose content is fixed. Modification requires an explicit Architectural Amendment and a newly recorded hash.

Superseded

An artifact replaced by a later governing artifact and carrying no current normative authority.

Retired

An artifact intentionally withdrawn without a replacement and carrying no current normative authority.

---

## Governing Artifacts

| Document | Status | Effective Date | SHA-256 | Governing Scope |
| --- | --- | --- | --- | --- |
| S1_CHARTER.md | Frozen | 2026-07-17 | 3AD056ADE476AF67DE6DF6E1E143C2B0EB8F11EF808732D42CDB36AF3C4FBB3F | mission, public purpose, and boundaries of NAV; Review: CA-001, CA-002 |
| VERDICT_TAXONOMY.md | Frozen | 2026-07-17 | 9F053C789EC4FC475425AFA0DFFE7EB233AA8332C3314D4AA73F0B9CB73344A6 | verification findings, output summaries, authorization decisions, policy, constraints, and execution accountability |
| SPEC.md | Frozen | 2026-07-17 | C400417A7B191BA9B5F00A4FA6B577D3081445C8C80EDE82B046DF7476B433D2 | current normative certificate representation and validation requirements; Review: CR-004 |
| GOVERNANCE.md | Frozen | 2026-07-17 | E817EE62BBF3729A3E7B2C0A70D346AAAED3F0EDAA506B4CC7DA4C4449BEA587 | governance and maintenance of the NAV standard |

---

## Governing Precedence

1. GOVERNANCE.md governs change procedure and maintenance authority.
2. VERDICT_TAXONOMY.md governs semantic meaning.
3. SPEC.md governs normative technical representation and validation within its published version.
4. S1_CHARTER.md governs mission, purpose, and scope.

These authorities govern different concerns and should ordinarily not conflict.

Where two governing artifacts appear to conflict:

1. Pause the affected standards or implementation work.
2. Determine whether the conflict is semantic, technical, procedural, or scope-related.
3. Apply the artifact governing that concern.
4. If the conflict cannot be resolved by scope, issue an explicit Architectural Amendment before work resumes.

Do not give a future or nonexistent artifact current precedence.

---

## Supporting and Historical Artifacts

| Artifact | Classification | Authority |
| --- | --- | --- |
| GOVERNANCE_v1.0.md | Superseded constitutional artifact | Permanent append-only history |
| S0_REPORT.md | Validation record | Non-normative |
| S1_DRAFT_REPORT.md | Drafting record | Non-normative |
| nav-cert-validator\ | Reference validator and examples | Non-normative except where SPEC.md explicitly makes a test or behavior normative |

Supporting artifacts may demonstrate conformance, history, or implementation behavior. They do not independently define NAV doctrine.

---

## Future Artifacts

Future artifacts, including an S2 Conformance Specification, Certificate Schema v2, certification program, and later reference implementations, acquire authority only after they exist and are explicitly classified in this registry.

Planned work is not governing doctrine.

Silence is not authority. The absence of a rule does not authorize the invention of a new NAV concept.

---

## Amendment Rule

Frozen governing artifacts may be modified only through an approved Architectural Amendment.

An amendment shall identify:

- the artifact being changed
- the reason for the change
- the prior hash
- the replacement hash
- the effective date
- affected dependent specifications or implementations

Ordinary implementation work, documentation maintenance, release activity, and conformance testing shall not silently modify governing doctrine.

---

## Implementation Principle

The specification describes demonstrated and approved reality.

Implementation conforms to doctrine.

Doctrine does not drift to accommodate implementation defects.

Observed evidence supersedes assumptions.

---

End of Document
