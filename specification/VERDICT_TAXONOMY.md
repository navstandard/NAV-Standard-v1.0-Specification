# VERDICT_TAXONOMY.md

Ruling of record: verdict, authorization, and execution-accountability semantics

Thirty Seven Inc. / VARI / the NAV standard (Network Attached Verification)

Ruling date: 2026-07-13

## 1. Status and authority

This document records a frozen architectural ruling for verdict, authorization, and execution-accountability semantics.

It distinguishes doctrine frozen now, current implementation, and planned realization. It does not implement certificate schema v2, gate release v14, execution receipts, policy evaluation, new validator behavior, or runtime changes.

The existing gate and NAV Certificate Format v1 remain unchanged.

## 2. Five-layer architecture

The architecture has five layers:

1. Atomic assertion extraction.
2. Assertion-level evidence findings.
3. Mechanically derived output-level verification summary.
4. Pinned institutional authorization policy and execution decision.
5. External execution receipt.

The Source of Record and evidence packet are inputs beneath the findings layer. They are not an additional verdict layer.

## 3. Assertion-level findings

Assertion-level findings are domain-neutral. The frozen finding vocabulary contains exactly four values.

| Finding | Meaning |
| --- | --- |
| `SUPPORTED` | The designated Source of Record contains cited evidence affirming the atomic assertion. |
| `CONTRADICTED` | The designated Source of Record contains cited evidence conflicting with the atomic assertion. |
| `UNVERIFIED` | The record was evaluated, but its evidence was insufficient to support or contradict the assertion. |
| `NOT_EVALUATED` | Evaluation did not complete because of parse failure, timeout, infrastructure failure, or equivalent operational failure. |

`UNVERIFIED` is a substantive and successful verification outcome. It honestly reports that sufficient evidence could not be established from the identified Source of Record.

`NOT_EVALUATED` must never be converted into `UNVERIFIED` or another substantive finding.

The distinction is permanent:

- `UNVERIFIED` means the evidence was insufficient after evaluation.
- `NOT_EVALUATED` means evaluation did not finish.

Atomic assertions cannot be partially supported. If an apparently atomic assertion is only partly supported, decomposition was inadequate. Partial support is an aggregate property, not an assertion-level finding.

## 4. Output-level verification summary

The output-level verification summary uses exactly four values:

- `FULLY_SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `CONTRADICTED`
- `UNVERIFIABLE`

The output summary is derived mechanically from the assertion findings.

No model, reviewer, or operator authors the summary.

A relying party must eventually be able to recompute it independently.

This document does not freeze the detailed precedence and derivation algorithm. The exact derivation table is required S2 / certificate-schema-v2 work and must be established against real artifacts and enumerated edge cases.

## 5. Execution decisions

Execution decisions belong to the policy layer. The frozen policy-layer decision vocabulary contains exactly four values.

| Decision | Meaning |
| --- | --- |
| `AUTHORIZED` | The pinned institutional policy permits automatic execution of the certified scope. |
| `AUTHORIZED_WITH_CONSTRAINTS` | The pinned institutional policy permits automatic execution only within the machine-readable constraints carried by the certificate. |
| `WITHHELD` | Automatic execution is not authorized. The request remains open for human disposition, with findings and evidence attached. |
| `REFUSED` | The pinned institutional policy prohibits execution of the certified request. Do not execute. |

`WITHHELD` and `REFUSED` must remain operationally distinct:

- `WITHHELD` stays open to a person.
- `REFUSED` is a policy-level stop on the certified request itself.

A person may later initiate a new request under a different authority or policy, but the refused certified request remains closed.

## 6. Fail-closed constraint handling

An agent that cannot recognize, interpret, or enforce every applicable constraint must treat the execution decision as `WITHHELD`.

Constraints are machine-readable directives, not narrative warnings.

The following examples are non-normative until S2:

- `verified_scope_only`
- `no_deletions`
- `read_only`
- `logging_required`
- `post_execution_notification`
- `maximum_transaction_value`
- `approved_record_types_only`

## 7. Pinned institutional policy

The execution decision comes from the institution's own pinned authorization policy.

The policy is:

- named,
- versioned,
- immutable for the certificate that cites it,
- cryptographically hashed.

Minimum planned certificate-v2 policy fields:

- `policy_id`
- `policy_version`
- `policy_hash`

The following optional fields are reserved for S2 consideration:

- `policy_issuer`
- `policy_effective_date`
- `policy_evaluation_result`

NAV does not determine institutional risk appetite. It records the execution decision produced by applying the institution's identified and hashed policy to the verification record.

The institution decided when it approved and pinned the policy.

NAV faithfully records and attributes the resulting decision.

## 8. Current implementation alignment and known gaps

This doctrine was derived from demonstrated appliance behavior and known gaps rather than invented on a whiteboard.

The following behaviors have been demonstrated in the current appliance:

- atomic decomposition of compound output,
- assertion-by-assertion evidence evaluation,
- cited supporting or contradicting passages,
- `UNVERIFIED` discipline rather than manufacturing refutation from silence,
- deterministic worst-signal finalization,
- fail-closed authority handling before adjudication.

Current appliance behavior already embodies one implicit policy: the default maximally conservative worst-signal finalization rule.

Certificate schema v2 does not introduce institutional policy into the architecture. It externalizes the single implicit policy already embodied by the appliance into an explicit, attributable artifact that institutions may later replace with their own pinned policies.

That policy is currently hardcoded in the gate rather than represented as a separately named and hashed customer-selectable artifact.

Certificate schema v2 does not invent a policy layer where none existed. It extracts the existing implicit policy into an explicit, attributable artifact and permits future institution-specific pinned policies.

Current certificate-v1 artifacts do not contain:

- a separate output-summary field,
- a policy ID, version, or hash,
- enforceable machine-readable constraints,
- first-class `NOT_EVALUATED` findings,
- execution receipts.

The following are known planned gaps:

- no separate certificate-v1 output-summary field,
- no separately pinned policy artifact,
- no enforceable machine-readable constraint set,
- no execution receipt,
- no first-class `NOT_EVALUATED` artifact category.

Current parse, timeout, and infrastructure failures are handled fail-closed but are not emitted today as a first-class `NOT_EVALUATED` artifact category. First-class `NOT_EVALUATED` recording is planned for certificate schema v2 / gate release v14.

## 9. Certificate / execution-receipt boundary

The certificate records what was authorized.

The execution receipt records what was executed.

No receipt means no claim that execution occurred.

VARI produces the verification record and certificate.

Execution occurs outside VARI.

The consuming system is responsible for producing the linked execution receipt.

VARI cannot attest that external execution occurred merely because authorization was issued.

The NAV standard may define a receipt format and may require conforming deployments to produce receipts, but the appliance must not claim to have witnessed execution unless it actually did.

## 10. Scope linkage

Future linkage is architectural intent.

Certificate fields may include:

- `certificate_id`
- `authorized_scope_hash`
- `decision`
- `constraints`
- `policy_id`
- `policy_hash`

Execution receipt fields may include:

- `certificate_id`
- `executed_scope_hash`
- `execution_timestamp`
- `executing_system`
- `outcome`
- `exception_record`
- `receipt_hash`

Hash equality alone proves that the same canonical scope representation was referenced.

S2 must define scope canonicalization precisely before any claim that scope conformance is mechanically established.

Until canonicalization is normative and implemented, scope linkage is architectural intent, not a demonstrated capability.

## 11. Retired vocabulary

The following terms are retired for future architecture. Historical artifacts containing retired tokens remain valid artifacts of their original schema and era. They are not retroactively invalidated.

| Retired term | Successor |
| --- | --- |
| `MATERIAL_DEFECT` | `CONTRADICTED`, at the finding or summary layer as applicable. |
| `HALLUCINATION_DETECTED` | `CONTRADICTED` or `UNVERIFIED` according to the evidence. |
| `VERIFIED_WITH_LIMITATIONS` | A separate verification summary plus, where execution is permitted conditionally, `AUTHORIZED_WITH_CONSTRAINTS`. |
| `AUTHORIZED_WITH_LIMITATIONS` | `AUTHORIZED_WITH_CONSTRAINTS`. |

`MATERIAL_DEFECT` is domain-scented and imprecise.

`HALLUCINATION_DETECTED` overclaims model psychology. VARI can establish conflict or absence of support in a designated record, not why a model generated the assertion.

`VERIFIED_WITH_LIMITATIONS` improperly collapsed evidence status and execution permission.

Limitation describes uncertainty. Constraint describes permitted machine behavior and can be enforced.

## 12. S0 continuity mapping

This table is a compatibility bridge, not a claim of exact semantic identity.

| S0 term | v2 architecture |
| --- | --- |
| S0 `VERIFIED` at assertion level | v2 `SUPPORTED` |
| S0 `VERIFIED_WITH_LIMITATIONS` | No exact one-to-one mapping; v2 separates verification summary from execution decision and constraints. |
| S0 `MATERIAL_DEFECT` | v2 `CONTRADICTED` |
| S0 `HALLUCINATION_DETECTED` | v2 `CONTRADICTED` or `UNVERIFIED` according to recorded evidence. |
| S0 `UNVERIFIED` / `UNVERIFIABLE` | v2 `UNVERIFIED` at assertion level / `UNVERIFIABLE` at output-summary level. |
| S0 `AUTHORIZED` | v2 `AUTHORIZED` |
| S0 `AUTHORIZED_WITH_LIMITATIONS` | v2 `AUTHORIZED_WITH_CONSTRAINTS` |
| S0 `WITHHELD_UNVERIFIABLE` | v2 output summary `UNVERIFIABLE` plus execution decision `WITHHELD`. |
| S0 `REFUSED` | v2 `REFUSED` |

Current parse, timeout, and infrastructure failures are handled fail-closed but are not emitted today as a first-class `NOT_EVALUATED` artifact category. First-class `NOT_EVALUATED` recording is planned for certificate schema v2 / gate release v14.

## 13. Release sequencing

S0 and certificate schema v1 remain unchanged.

S1 cites this ruling at the principle level.

S2 defines normative summary derivation, policy requirements, constraint vocabulary, certificate schema v2, receipt format, and canonicalization.

Gate release v14 implements certificate schema v2.

v14 also carries the already-standing provenance, parse-failure-category, and hard-timeout items, subject to the existing release and qualification process.

No current deployment may claim schema-v2 or S2 conformance before those artifacts exist.

This is not a separate new workstream. It defines the final architectural scope of the already-planned v14 release.

## 14. Closing architecture statement

AI generates.

VARI verifies and reports assertion-level findings.

A mechanical output summary is derived from those findings.

The institution's pinned policy converts the verification record into an execution decision.

The certificate carries evidence and authorization; the external execution receipt records what actually occurred.

Agents execute only within the authorization given.

The chain from machine output to institutional action is attributable at every link, and every artifact that governs the chain is pinned by hash.
