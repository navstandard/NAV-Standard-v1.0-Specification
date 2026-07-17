# Network Attached Verification (NAV) Certificate Format v1

Document token: `NAV-CERT-1`

License: CC-BY 4.0. Attribution: Thirty Seven Inc.

## Status

This document is the normative definition of the NAV Certificate Format v1.
It was derived from artifacts of the VARI reference implementation so that
v1 describes certificates as they actually exist; the derivation record
appears in the non-normative appendix. This document, not any
implementation, is normative. Where an implementation and this
specification disagree, this specification governs.

The implementation-emitted value of `certificate_version` for v1
certificates is `vari-gate-cert-1`. Validators MUST accept that value
exactly for v1 certificates.

## Normative Language

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD
NOT, RECOMMENDED, MAY, and OPTIONAL in this document are to be interpreted
as described in RFC 2119.

## Scope

A NAV certificate attests that a specific output was evaluated against a
named authority snapshot and records the resulting assertion verdicts,
decision, and certificate integrity hash. It does not attest to model
quality, prompt design, benchmark performance, or the internal process used
to earn a verdict.

Attribution of semantic content: all semantic fields in a certificate
(verdicts, reasoning, passages, the decision) are issuer-recorded claims.
The certificate attests what the issuing gate concluded against the named
authority snapshot; it is not an assertion of independent truth.

## Certificate Object

Unknown fields MUST be ignored by v1 validators and MUST NOT cause
validation failure.

| Field | Type | Required | Semantics |
| --- | --- | --- | --- |
| `certificate_version` | string | yes | v1 value: `vari-gate-cert-1`. |
| `gate_version` | string | yes | Identifier of the issuing gate implementation. |
| `issued_at` | string | yes | Issuance timestamp, ISO 8601. v1 validators do not validate timestamp format. |
| `certificate_id` | string | yes | Issuer-generated certificate identifier. |
| `action` | object | yes | Identifies the evaluated output. |
| `authority` | object | yes | Identifies the authority record snapshot used at issuance. |
| `mode` | string | yes | Evaluation mode. See Mode. |
| `assertions` | array | yes | List of assertion adjudication records, in issuer order. Order is not semantically significant. |
| `decision` | string | yes | Final authorization disposition derived from the recorded verdicts. See Decision Taxonomy. |
| `integrity_sha256` | string | yes | Lowercase hexadecimal SHA-256 over the canonical certificate body excluding this field. |

### `action`

| Field | Type | Required | Semantics |
| --- | --- | --- | --- |
| `output_id` | string | yes | Identifier of the evaluated output. |
| `output_sha256` | string | yes | Lowercase hexadecimal SHA-256 of the evaluated output content as computed by the issuing gate. v1 offline validators cannot independently validate this without the original output content. |

### `authority`

| Field | Type | Required | Semantics |
| --- | --- | --- | --- |
| `authority_id` | string | yes | Issuer-recorded authority identifier (for example, a policy document name). |
| `snapshot_sha256` | string | yes | Lowercase hexadecimal SHA-256 of the authority record text as computed at designation time. |

### Assertion Record

| Field | Type | Required | Semantics |
| --- | --- | --- | --- |
| `assertion` | string | yes | Assertion text adjudicated by the gate. |
| `verdict` | string | yes | One of the verdict tokens listed below. |
| `method` | string | yes | Method label emitted by the gate for this assertion. |
| `reasoning` | string | yes | Issuer-recorded rationale for the verdict. |
| `supporting_passage` | string or null | yes | Authority text passage used as support, or null when no passage supports the assertion. |
| `evidence_sha256` | string | yes | Lowercase hexadecimal SHA-256 over the evidence material selected by the gate for this assertion. |
| `retrieval_count` | integer | yes | Count of retrieved authority passages considered for the assertion. |

## Mode

`mode` records the evaluation mode under which the certificate was issued.
v1 values:

| Mode | Semantics |
| --- | --- |
| `llm` | Adjudication was performed by the issuing gate's model configuration. |
| `offline` | Adjudication was NOT performed by models. Offline-mode certificates are test and integration artifacts. |

Relying parties MUST examine `mode`. Production reliance SHOULD be limited
to `llm`-mode certificates. An offline-mode certificate carries valid
structure and integrity but does not represent a model-exercised
evaluation.

## Verdict Taxonomy

Verdicts describe the evaluation of individual assertions.

| Verdict | Semantics |
| --- | --- |
| `VERIFIED` | Supported by the authority evidence. |
| `VERIFIED_WITH_LIMITATIONS` | Supported, with a missing, softened, or qualified condition. |
| `MATERIAL_DEFECT` | Materially inconsistent with the authority evidence. Fail-closed. |
| `HALLUCINATION_DETECTED` | Positively contradicted by, or fabricated relative to, the authority evidence. Fail-closed. |
| `UNVERIFIED` | Not verifiable from the authority evidence. A first-class disposition; fail-closed to withheld authorization. |

## Decision Taxonomy

Exactly one decision applies to every certificate. The decision is derived
from the recorded assertion verdicts by worst-signal precedence: the most
severe verdict present determines the decision. Severity order, most severe
first: `MATERIAL_DEFECT` and `HALLUCINATION_DETECTED` (equal severity),
then `UNVERIFIED`, then `VERIFIED_WITH_LIMITATIONS`, then `VERIFIED`.

| Decision | Derivation |
| --- | --- |
| `AUTHORIZED` | All recorded assertions are `VERIFIED`. |
| `AUTHORIZED_WITH_LIMITATIONS` | Worst recorded assertion is `VERIFIED_WITH_LIMITATIONS`. |
| `WITHHELD_UNVERIFIABLE` | No assertions are recorded, or the worst recorded assertion is `UNVERIFIED`. Fail-closed. |
| `REFUSED` | Worst recorded assertion is `MATERIAL_DEFECT` or `HALLUCINATION_DETECTED`. Fail-closed. |

## Canonical Serialization and Integrity Hash

Canonical serialization and integrity validation SHALL be performed as follows:

1. Remove the top-level `integrity_sha256` field from the certificate
   object.
2. Serialize the remaining object as JSON with keys sorted recursively.
3. Use compact separators: comma `,` and colon `:`, with no insignificant
   whitespace.
4. Preserve Unicode characters as characters rather than ASCII escapes.
5. Encode the serialized JSON as UTF-8.
6. Compute SHA-256 over those bytes.
7. Compare the lowercase hexadecimal digest to the original top-level
   `integrity_sha256`.

## Offline Validation Procedure

A relying party validating only the certificate and this specification
performs these steps:

1. Parse the certificate as JSON.
2. Confirm the required top-level fields are present with the types defined
   above.
3. Confirm required nested `action`, `authority`, and `assertions[]` fields
   are present with the types defined above.
4. Confirm `verdict`, `decision`, and `mode` values are in the v1
   taxonomies.
5. Ignore unknown fields.
6. Recompute `integrity_sha256` using the canonical serialization and
   hashing rules above.
7. Treat the certificate as valid only if schema validation and integrity
   validation both pass.
8. OPTIONAL: if a copy of the authority record is available, hash its UTF-8
   text and compare the digest to `authority.snapshot_sha256`.
9. OPTIONAL: recompute the decision from the recorded verdicts using the
   worst-signal precedence defined in Decision Taxonomy and compare it to
   the certificate's `decision`. A mismatch indicates that the certificate
   is internally inconsistent, even where its integrity hash verifies.

The v1 offline procedure does not validate `action.output_sha256` without
the original evaluated output content.

Example certificates are illustrative only and do not supersede this
specification.

## Versioning and Forward Compatibility

NAV Certificate Format v1 certificates validate forever under the v1 rules
above. A future v2 extension is reserved as an additive extension. Unknown
fields are ignored, never errors, so additive fields do not break v1
validation. Breaking changes require a new major version.

Non-normative note: the vocabulary and structure planned for v2 are
governed by the architecture ruling VERDICT_TAXONOMY.md.

## Appendix A (non-normative): Derivation Record

This specification was derived from the following reference-implementation
artifacts, recorded here as evidence that v1 describes certificates as
actually emitted:

- Reference source certificate:
  `run_gov_config_v13_confirm_20260713/cert_OUT-006.json`,
  SHA-256 `c0b244f8fd64dfebe319f90d9c840cf16361c1cae74c25d3041c27c7145e3a12`.
- Verdict token list, decision derivation, and canonicalization behavior
  derived from the reference gate and validator sources at the versions
  hashed in the qualification records.
- Token exhibition status at derivation time: `VERIFIED`,
  `VERIFIED_WITH_LIMITATIONS`, `UNVERIFIED`, `MATERIAL_DEFECT`,
  `AUTHORIZED_WITH_LIMITATIONS`, `WITHHELD_UNVERIFIABLE`, `REFUSED`, and
  `AUTHORIZED` are each exhibited by at least one retained run artifact.
  `HALLUCINATION_DETECTED` is defined by the implementation's verdict list
  but not exhibited by any retained certificate artifact at derivation
  time.
