# NAV Certificate Validator

Network Attached Verification (NAV) certificates record the assertion verdicts, final decision, authority snapshot, and integrity hash emitted by the VARI reference implementation; spec DOI placeholder: `TBD`, paper link placeholder: `TBD`.
This repository validates NAV Certificate Format v1 JSON files by checking required schema fields and recomputing `integrity_sha256`.
Run `python validate_nav_c.py examples/valid_certificate.json` for the CLI validator, or open `validator.html` locally and drop or paste a certificate JSON.
