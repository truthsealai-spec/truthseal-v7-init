#!/usr/bin/env bash
# anchor_ots.sh — anchors a given receipt with OpenTimestamps CLI
# Usage: ./governance/scripts/anchor_ots.sh governance/ledger/receipts/<receipt.json>
set -euo pipefail
rec="$1"
ots stamp "$rec"
echo "Stamped. If you get a .ots file, place it alongside the receipt."
echo "When anchored, update the JSON fields: ots_status, ots_tx, anchor_utc."
