# TruthSeal™ v6.9.3 — Ledger Binding + Entitlement Gates + Admin Policy Screen

## Purpose
Bind every Verdict Card™ to a tamper-evident record and add role-based access so only approved roles can view admin controls.

## What this enables
- **Ledger Binding:** every result gets a hash + UTC timestamp + transaction ID.
- **Entitlement Gates:** Viewer / Analyst / Admin role separation.
- **Admin Policy Screen:** toggles providers, shows time-sync, and handles compliance links.

## Minimal Fields
- `case_id`, `verdict_hash`, `timestamp_utc`, `timestamp_local`, `timezone`
- `role_required`, `tx_id`, `sync_integrity`

## Validation Rules
- `sync_integrity` = OK or block write
- `timestamp_utc` within ±120 s of server UTC
- Role must match access gate

## Commit message
Add ledger binding spec + role gates + admin policy screen (v6.9.3)
