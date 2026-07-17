#!/usr/bin/env python3
"""Validate NAV Certificate Format v1 JSON files.

Usage:
    python validate_nav_c.py certificate.json [authority_file]

Exit status is 0 for PASS and 1 for FAIL.
"""

import hashlib
import json
import sys


VERDICTS = {
    "VERIFIED",
    "VERIFIED_WITH_LIMITATIONS",
    "MATERIAL_DEFECT",
    "HALLUCINATION_DETECTED",
    "UNVERIFIED",
}

DECISIONS = {
    "AUTHORIZED",
    "AUTHORIZED_WITH_LIMITATIONS",
    "WITHHELD_UNVERIFIABLE",
    "REFUSED",
}

HEX64 = set("0123456789abcdef")


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def is_hex64(value):
    return isinstance(value, str) and len(value) == 64 and all(c in HEX64 for c in value)


def require_type(errors, obj, key, typ, path):
    if key not in obj:
        errors.append(f"{path}.{key}: missing required field")
        return None
    value = obj[key]
    if not isinstance(value, typ):
        errors.append(f"{path}.{key}: expected {typ.__name__}")
        return None
    return value


def validate_schema(cert):
    errors = []
    if not isinstance(cert, dict):
        return ["$: expected object"]

    require_type(errors, cert, "certificate_version", str, "$")
    require_type(errors, cert, "gate_version", str, "$")
    require_type(errors, cert, "issued_at", str, "$")
    require_type(errors, cert, "certificate_id", str, "$")
    require_type(errors, cert, "mode", str, "$")
    decision = require_type(errors, cert, "decision", str, "$")
    integrity = require_type(errors, cert, "integrity_sha256", str, "$")

    if cert.get("certificate_version") != "vari-gate-cert-1":
        errors.append("$.certificate_version: expected vari-gate-cert-1")
    if decision is not None and decision not in DECISIONS:
        errors.append("$.decision: unknown decision")
    if integrity is not None and not is_hex64(integrity):
        errors.append("$.integrity_sha256: expected lowercase sha256 hex")

    action = require_type(errors, cert, "action", dict, "$")
    if action is not None:
        require_type(errors, action, "output_id", str, "$.action")
        output_hash = require_type(errors, action, "output_sha256", str, "$.action")
        if output_hash is not None and not is_hex64(output_hash):
            errors.append("$.action.output_sha256: expected lowercase sha256 hex")

    authority = require_type(errors, cert, "authority", dict, "$")
    if authority is not None:
        require_type(errors, authority, "authority_id", str, "$.authority")
        snap = require_type(errors, authority, "snapshot_sha256", str, "$.authority")
        if snap is not None and not is_hex64(snap):
            errors.append("$.authority.snapshot_sha256: expected lowercase sha256 hex")

    assertions = require_type(errors, cert, "assertions", list, "$")
    if assertions is not None:
        for i, assertion in enumerate(assertions):
            path = f"$.assertions[{i}]"
            if not isinstance(assertion, dict):
                errors.append(f"{path}: expected object")
                continue
            require_type(errors, assertion, "assertion", str, path)
            verdict = require_type(errors, assertion, "verdict", str, path)
            require_type(errors, assertion, "method", str, path)
            require_type(errors, assertion, "reasoning", str, path)
            if "supporting_passage" not in assertion:
                errors.append(f"{path}.supporting_passage: missing required field")
            elif assertion["supporting_passage"] is not None and not isinstance(assertion["supporting_passage"], str):
                errors.append(f"{path}.supporting_passage: expected string or null")
            evidence = require_type(errors, assertion, "evidence_sha256", str, path)
            retrieval_count = require_type(errors, assertion, "retrieval_count", int, path)
            if verdict is not None and verdict not in VERDICTS:
                errors.append(f"{path}.verdict: unknown verdict")
            if evidence is not None and not is_hex64(evidence):
                errors.append(f"{path}.evidence_sha256: expected lowercase sha256 hex")
            if retrieval_count is not None and retrieval_count < 0:
                errors.append(f"{path}.retrieval_count: expected non-negative integer")

    return errors


def validate_certificate(cert):
    errors = validate_schema(cert)
    body = {k: v for k, v in cert.items() if k != "integrity_sha256"} if isinstance(cert, dict) else {}
    computed = sha256_text(canonical(body))
    claimed = cert.get("integrity_sha256") if isinstance(cert, dict) else None
    integrity_ok = computed == claimed
    if not integrity_ok:
        errors.append("$.integrity_sha256: does not match canonical certificate body")
    return computed, errors


def main(argv):
    if len(argv) not in (2, 3):
        print(__doc__.strip())
        return 1

    try:
        with open(argv[1], encoding="utf-8") as f:
            cert = json.load(f)
    except Exception as exc:
        print(f"FAIL: cannot parse certificate JSON: {exc}")
        return 1

    computed, errors = validate_certificate(cert)
    authority_ok = None
    if len(argv) == 3 and isinstance(cert, dict):
        try:
            with open(argv[2], encoding="utf-8") as f:
                authority_text = f.read()
            authority_ok = sha256_text(authority_text) == cert.get("authority", {}).get("snapshot_sha256")
            if not authority_ok:
                errors.append("$.authority.snapshot_sha256: authority file does not match")
        except Exception as exc:
            errors.append(f"authority file: {exc}")

    if errors:
        print("FAIL")
        print(f"computed_integrity_sha256: {computed}")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print(f"computed_integrity_sha256: {computed}")
    print(f"decision: {cert['decision']}")
    print(f"assertions: {len(cert['assertions'])}")
    if authority_ok is not None:
        print("authority_snapshot: MATCH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
