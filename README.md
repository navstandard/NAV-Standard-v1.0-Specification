# NAV Standard v1.0 Publication Candidate

Status: Publication Candidate. NAV Standard v1.0 has not been declared published.

NAV stands for Network Attached Verification. NAV defines a certificate format and validation requirements for accountable verification against authority evidence.

NAV addresses a narrow problem: machine-generated output may influence institutional decisions, and institutions need portable evidence showing how that output was checked against an identified authority record.

A NAV certificate records an evaluated output, the authority snapshot used, assertion-level verdicts, a decision value, and an integrity hash. Certificate integrity validation confirms that the certificate body matches its recorded hash. It does not establish the factual truth of a claim, issuer identity, digital-signature authenticity, or certification status.

## Normative Documents

The normative publication-candidate documents are in `specification/`:

- `S1_CHARTER.md`
- `GOVERNANCE.md`
- `SPEC.md`
- `VERDICT_TAXONOMY.md`
- `ARCHITECTURE_REGISTRY.md`

If non-normative materials conflict with these frozen documents, the frozen documents control.

## Validation

Use the Python validator:

```powershell
python validator\validate_nav_c.py examples\valid_certificate.json
```

Or open `validator/validator.html` locally and paste or drop a certificate JSON file.

The validator checks required fields, known v1 taxonomy values, and certificate integrity. It does not verify issuer authentication, digital signatures, factual truth, or public certification status.

## Examples

Example certificates are in `examples/`. Their documentation is non-normative and cannot override `specification/SPEC.md`.

## Not Yet Available

Conformance and certification programs are not yet published. VARI Verified must not be presented as currently available certification under the public NAV program.
