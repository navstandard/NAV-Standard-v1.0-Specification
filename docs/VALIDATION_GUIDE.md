# Validation Guide

Non-normative practical guide.

## Inspect a Certificate

Open the JSON certificate and identify `certificate_version`. NAV Certificate Format v1 uses `vari-gate-cert-1`.

## Validate Integrity

Follow `specification/SPEC.md` section "Canonical Serialization and Integrity Hash":

1. Remove `integrity_sha256`.
2. Canonically serialize the remaining certificate body as specified.
3. Compute SHA-256 over the UTF-8 bytes.
4. Compare the computed digest to the recorded `integrity_sha256`.

## Use the Supplied Validator

Run:

```powershell
python validator\validate_nav_c.py examples\valid_certificate.json
```

The validator reports pass or fail and prints computed integrity details.

## Interpret Results

A passing integrity check does not prove issuer identity, digital-signature authenticity, factual truth, or certification status.

## Examples

The `examples/` directory includes one valid certificate and examples that demonstrate stale integrity, bad integrity, and missing required fields.
