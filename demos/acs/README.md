# TruthSeal™ ACS Demo — Local Receipt Generator (v1.0)

**Purpose:** Show, offline, how we hash any input text and produce a lightweight **receipt**.  
**Scope:** Demo only (no blockchain). For real anchoring, queue OpenTimestamps when services are live.

---

## How to use (3 steps)
1) Open `demos/acs/ACS_Receipt_Demo.html` in your browser (double-tap in GitHub → “Raw” → open locally).
2) Paste any text → tap **Generate** to compute the SHA-256 → tap **Copy** (or **Download JSON**, if shown).
3) Store the receipt under `governance/ledger/receipts/` (or a `receipts/` folder when present).

---

## Receipt (example JSON)
```json
{
  "input_sha256": "<sha256_of_your_text>",
  "created_utc": "<ISO8601>",
  "tool": "TruthSeal ACS Demo v1.0 (local)",
  "notes": "Local demo only — not a blockchain timestamp"
}
