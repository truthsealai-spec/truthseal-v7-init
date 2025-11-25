#!/usr/bin/env python3
# ACS_Receipt_Generator_v1.py — builds a PQC-ready receipt JSON from CORE_TQC_TEST summary
# Usage: python3 governance/tools/ACS_Receipt_Generator_v1.py <summary_json_path>

import os, sys, json, hashlib, datetime as dt, pathlib

def iso_now():
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def write_receipt(artifact_path, artifact_sha):
    out_dir = pathlib.Path("governance/ledger/receipts")
    out_dir.mkdir(parents=True, exist_ok=True)

    base_name = f"{dt.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}__ACS_Receipt_v1.0__sha256_{artifact_sha[:12]}.json"
    out_path = out_dir / base_name

    receipt = {
        "artifact_path": str(artifact_path),
        "sha256": artifact_sha,
        "created_utc": iso_now(),
        "source": "CORE_TQC_TEST_v1 → ACS_Receipt_v1.0",
        "note": "ACS receipt binds TQC stress test results; LEI=1 enforced in runtime policy.",
        "ots_status": "pending",
        "ots_calendar_id": "",
        "ots_receipt_path": str(out_dir / (base_name.replace(".json", ".ots"))),
        "ots_tx": "",
        "anchor_utc": ""
    }
    with open(out_path, "w") as f:
        json.dump(receipt, f, indent=2)
    print(f"Wrote receipt: {out_path}")
    return out_path

def main():
    if len(sys.argv) != 2:
        print("Usage: ACS_Receipt_Generator_v1.py <summary_json_path>")
        sys.exit(1)
    summary_path = pathlib.Path(sys.argv[1]).resolve()
    if not summary_path.exists():
        raise SystemExit(f"Not found: {summary_path}")

    artifact_sha = sha256_file(summary_path)
    rec_path = write_receipt(summary_path, artifact_sha)

    print("\nNext (when OTS is live):")
    print(f"  ots stamp {rec_path}")
    print(f"  # store the .ots at: governance/ledger/receipts/ (same folder)")
    print("  # then update ots_status→'anchored', add ots_tx + anchor_utc")

if __name__ == "__main__":
    main()
