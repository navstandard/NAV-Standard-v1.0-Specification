# Examples

`valid_certificate.json` is a real certificate copied from `run_gov_config_v13_confirm_20260713/cert_OUT-006.json` without scrubbing; no internal username or local path strings were present.

`tampered_content.json` modifies a hashed field inside the certificate body while leaving `integrity_sha256` unchanged, so validators fail it by detecting stale integrity. NAV Certificate Format v1 does not include the original output content, so these validators cannot independently check whether `action.output_sha256` matches an external output body.

`bad_integrity.json` changes only `integrity_sha256`, so validators fail it by recomputing the canonical body hash.

`wrong_schema.json` removes a required field, so validators fail it during schema validation.
