# GOVERNANCE.md
The NAV standard (Network Attached Verification)
Version 2.0 — Supersedes v1.0 (retained, hashed, see Amendment Log CA-001)
Author and decision authority: Thirty Seven Inc.

## 1. Purpose

This document defines how the NAV standard and its constitutional artifacts
change: who decides, what the artifact lifecycle is, what review and
amendment mean, and what adopters may rely on. It governs process only.
Mission lives in the Charter. Semantics live in VERDICT_TAXONOMY.md.
Technical requirements live in the specifications.

## 2. Authority

The NAV standard is authored and maintained by Thirty Seven Inc. Decisions
rest with the author. There is no committee. Proposals from any party are
welcome as issues against the public repository; every accepted or rejected
proposal of consequence receives a recorded disposition with rationale.
This arrangement is stated plainly because adopters deserve to know how
decisions are made, and a named accountable author is a stronger promise
than an imagined committee.

## 3. Constitutional artifacts and the registry

The constitutional set is enumerated in ARCHITECTURE_REGISTRY.md, which
records each artifact's name, version, lifecycle state, and hash. The
registry is the single source of truth for what governs. An artifact not in
the registry is not constitutional. Conflicts between artifacts are
resolved by the precedence order stated in the registry; where the registry
is silent, the more specific artifact governs the more general, and later
frozen artifacts govern earlier ones.

## 4. Artifact lifecycle

Every constitutional artifact is in exactly one state:

- DRAFT: under construction; carries no authority; may change freely.
- APPROVED: accepted by the author as correct; citable; may still receive
  editorial correction without ceremony, but no change of meaning.
- FROZEN: fixed and hashed; the artifact's meaning and text may not change.
  Any change of meaning requires an Architectural Amendment producing a new
  version; the frozen predecessor is never edited.
- SUPERSEDED: replaced by a newer version. The artifact remains in the
  registry with its hash. Superseded artifacts are never deleted; history
  is append-only.
- RETIRED: withdrawn without a successor. Retained and hashed like
  superseded artifacts.

Transitions: DRAFT to APPROVED by author acceptance; APPROVED to FROZEN by
author freeze declaration together with hash recording in the registry,
both required, effective when both complete; FROZEN to
SUPERSEDED only by an Architectural Amendment; any state to RETIRED by
author declaration with recorded rationale.

## 5. Architectural Reviews (CR-nnn)

An Architectural Review is a documented examination of one or more
constitutional artifacts, conducted or commissioned by the author,
producing a numbered record (CR-001, CR-002, ...) and a disposition:
ready to freeze, not ready with reasons, or amendment required. Reviews may
be performed by the author, by engaged architects, or by automated agents;
the disposition is always the author's. Review records are retained in the
repository.

## 6. Architectural Amendments (CA-nnn)

An Architectural Amendment is the only mechanism by which a FROZEN
artifact's meaning changes. An amendment is a numbered record (CA-001,
CA-002, ...) stating: the artifact and version amended, the change and its
rationale, the new version produced, the new hash, and the disposition of
the predecessor (superseded). Amendments are approved solely by the author.
The amendment log is append-only and lives beside the registry.

## 7. Versioning

Specifications and constitutional documents use semantic versioning.
A MAJOR version signals a breaking change: any change that could cause a
previously conforming artifact or implementation to become nonconforming,
or that changes the meaning of an existing field, term, or requirement.
A MINOR version signals an additive change: new optional fields, new
non-governing supporting documents, or clarifications that cannot change a
conforming implementation's status. The introduction of a new
constitutional artifact is not a versioning event at all: governing
documents enter the constitutional set only through the Architectural
Amendment process and registration in ARCHITECTURE_REGISTRY.md. Editorial corrections that change no meaning may be issued without
a version change while an artifact is APPROVED, and never while FROZEN.

## 8. Compatibility guarantees

Certificates valid under a published major version of the NAV certificate
format remain valid under that version forever. Validators must ignore
unknown fields rather than reject them. No future version of the standard
will retroactively invalidate artifacts produced in conformance with an
earlier published version. Backward compatibility is the default; breaking
changes require a MAJOR version and an explicit migration note.

## 9. Release artifacts and hashing

Every release of every constitutional artifact and specification is
published with its SHA-256 hash. Hashes are recorded in the registry and in
release tags. The standard's own paper trail is expected to meet the
evidentiary discipline the standard prescribes for others.

## 10. Reference implementation

VARI, by Thirty Seven Inc., is the reference implementation of the NAV
standard. Reference status means the implementation tracks the standard and
demonstrates its practicability; it does not mean the standard is defined
by the implementation's behavior. Where implementation and specification
disagree, the specification governs, and the disagreement is resolved by
correction or by amendment, recorded either way. Conformance of any
implementation, including the reference, is established by the conformance
specification when it exists, not by this document.

## 11. What this document does not do

It does not define verification semantics, certificate structure, or
conformance requirements. It does not describe roadmaps or planned
features; governance governs what exists. It does not create obligations
for implementers beyond the compatibility guarantees stated here.

## 12. Status

Version 2.0. APPROVED upon author acceptance. FROZEN only when both
conditions are met: the author's freeze declaration, and the artifact's
hash recorded in ARCHITECTURE_REGISTRY.md. Neither alone freezes an
artifact; the freeze is effective at whichever of the two completes last.

## Amendment Log

CA-001 (2026-07-16): GOVERNANCE.md v1.0 superseded by v2.0. Change: v1
defined versioning and authority only; v2 adds the artifact lifecycle,
Architectural Reviews, Architectural Amendments, compatibility guarantees,
release hashing, and the reference-implementation relationship, codifying
the constitutional machinery already in practice. v1 retained with its
hash in the registry. Approved: Thirty Seven Inc. This amendment is the
founding entry of the process it defines.
