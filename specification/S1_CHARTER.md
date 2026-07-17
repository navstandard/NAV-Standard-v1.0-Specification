# NAV Standard S1 Charter

## 1 Purpose

NAV exists to standardize how verification evidence and verification results are represented, communicated, exchanged, and validated.

Machine-generated output increasingly influences decisions carrying legal, financial, operational, regulatory, or safety consequences. Institutions remain accountable for those decisions. Before relying upon machine-generated output, institutions require evidence that demonstrates diligence before action.

NAV defines the open standard for that evidence. NAV is not the verification engine.

## 2 The Problem

AI systems can produce machine-generated output. They cannot assume institutional accountability.

Institutions decide whether and how to rely upon machine-generated output. Institutions remain accountable for those decisions.

Evidence is required before reliance because evidence demonstrates that the institution exercised diligence before acting. Evidence does not guarantee correctness.

NAV standardizes how verification evidence is represented.

## 3 Separation of Responsibilities

### AI Generates

AI produces machine-generated output.

AI does not verify its own output by assertion or confidence alone. AI does not assume institutional accountability.

### VARI Verifies

VARI is a verification engine that compares machine-generated output against authoritative Sources of Record.

VARI produces evidence, comparison, and verification results.

VARI does not determine truth, replace institutional judgment, make decisions, guarantee correctness, or certify AI systems.

### Institutions Decide

Institutions decide whether and how to rely upon machine-generated output.

Institutions remain accountable for those decisions.

## 4 Verification Model

Verification compares machine-generated output against an identified authoritative Source of Record.

The comparison produces evidence and a verification result.

Verification and institutional decision making are separate responsibilities.

NAV standardizes the representation and communication of verification evidence and verification results. It does not prescribe the institution's decision process or resulting action.

## 5 Source of Record

A Source of Record is the authoritative source against which a machine-generated assertion is compared.

Examples include a court opinion, signed contract, approved architecture document, approved codebase, official policy repository, ERP, ledger, regulated registry, or calibrated measurement system.

NAV does not determine whether an institution selected the correct Source of Record. NAV requires the Source of Record used for verification to be identified.

## 6 Verification Results

Verification produces standardized verification findings and results.

The meaning, semantics, and interpretation of those findings and results are governed by `VERDICT_TAXONOMY.md`.

This Charter establishes the purpose, scope, and boundaries of verification. It does not define individual verification outcomes.

## 7 Founding Principles

### Institutional Accountability

Institutions remain accountable for decisions influenced by machine-generated output.

Responsibility does not transfer to AI.

### Evidence Before Reliance

Evidence demonstrates that an institution exercised diligence before acting.

Evidence does not guarantee correctness.

### Source of Record Authority

Verification depends upon an identified Source of Record.

NAV requires the Source of Record used for verification to be identified. NAV does not determine whether the selected Source of Record is correct.

### Comparison Not Omniscience

VARI compares machine-generated output against an identified Source of Record.

VARI does not determine universal truth.

### Unable to Verify Is A Valid Result

The absence of sufficient evidence is a valid verification result.

The detailed meaning, interpretation, and treatment of that result are governed by `VERDICT_TAXONOMY.md`.

### Independent Verification

Verification must not depend solely upon the assertions or confidence of the system generating the output.

### Observable Behavior

NAV standardizes observable verification artifacts.

NAV does not prescribe implementation.

### Economy of Design

The NAV Standard SHALL remain as simple as possible while completely defining interoperable behavior. Complexity belongs in implementations and supporting documentation, not in the core standard.

## 8 Scope

NAV defines the representation and communication of verification performed by comparing machine-generated output against authoritative Sources of Record.

NAV defines how verification evidence and verification results are represented, communicated, exchanged, and validated.

## 9 What NAV Does Not Define

NAV does not define truth.

NAV does not define AI safety.

NAV does not define prompt engineering.

NAV does not define model evaluation.

NAV does not define decision making.

NAV does not define legal advice.

NAV does not define institutional policy.

NAV does not define general fact checking.

NAV does not define whether a Source of Record itself is correct.

## 10 Relationship Between VARI and NAV

VARI is a commercial verification engine and the originating reference implementation.

VARI performs verification and produces evidence.

NAV is an open standard.

NAV defines representation, interoperability, and communication of verification results.

Future conforming implementations may exist.

## 11 Relationship To S0

S0 defines the NAV Certificate Format v1 technical foundation.

S0 specifies certificate fields, emitted verdict and decision tokens, canonical serialization, integrity hashing, offline validation, versioning, and forward compatibility for NAV Certificate Format v1.

S1 states the charter and founding principles for the NAV Standard. It does not modify S0.

## 12 Status

This document is an S1 draft amended pursuant to Constitutional Review CR-002.

It remains pending final architectural review.

It does not modify the NAV Certificate Format v1 or introduce new technical conformance requirements.
