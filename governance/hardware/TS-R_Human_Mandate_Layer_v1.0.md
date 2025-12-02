# TruthSeal™ — TS-R Human Mandate Layer v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal specification for the Human Mandate Layer (HML) for TruthSeal
  Robotics Profiles TS-R1 (single robot) and TS-R2 (swarm / fleet).
  This document defines WHO is allowed to command robots and fleets, HOW
  authority is expressed, and HOW those decisions interact with TruthSeal
  laws, metrics, and receipts.

---

## 0. Core Concepts (expanded once)

- **Aim Coherence Score (ACS)** – 0–1 metric that measures how well actions follow the declared aim and safety constraints over time.
- **Traykov Coherence Score v0.1 (TCS v0.1)** – 0–1 metric for overall intelligence coherence (truthfulness, post-quantum security strength, long-horizon self-consistency).
- **Coherence Score (CHS)** – four-band status indicator:
  - CHS/L – Low (Red)
  - CHS/M – Medium (Yellow)
  - CHS/H – High (Green)
  - CHS/UH – Ultra High (Blue)
- **Traykov Law of Quantum Coherence (TQC)** – hardware-anchored law demanding monotonic improvement in coherence; no “free lunch” in risk.
- **Law of Ethical Irreversibility (LEI = 1)** – once a safer, more coherent option exists, the system must not downgrade to a riskier one.
- **TruthSeal Robotics Profile TS-R1** – robotics profile for a single robot executing actions under TruthSeal law.
- **TruthSeal Robotics Profile TS-R2** – robotics profile for a swarm or fleet of robots with quorum and split-brain rules.
- **TS-R Failure Modes & Fallback Law v1.0** – law ladder that defines downgrade and safe-stop behaviour driven by CHS bands and environment flags.
- **TS-R Receipt Schema v1.0** – robotics receipt specification that records CHS, ACS, TCS, environment, actors, law blocks, and anchoring.
- **Human Mandate Layer (HML)** – the set of roles, tokens, and rules that bind human authority to TS-R1 / TS-R2 behaviour without ever violating TQC or LEI = 1.

---

## 1. Purpose

The Human Mandate Layer ensures that:

1. Robots and fleets take commands only from **authorised humans and institutions**.
2. Human decisions are **bounded by TruthSeal laws** (TQC, LEI = 1, TS-R Failure Modes & Fallback Law).
3. Every important command is **proven later** via TS-R receipts and anchoring.

No human – including owners, guardians, regulators, or emergency services – can force a robot or fleet to violate LEI = 1 or TQC.

---

## 2. Roles

HML defines these roles:

- **Owner** – legal owner of the robot or fleet. Has broad configuration and approval rights within safety limits.
- **Guardian** – person explicitly delegated by the Owner (e.g. parent, caregiver). Can authorise or cancel actions near children, infants, or vulnerable people.
- **Operator** – day-to-day user (e.g. staff member, technician). Can issue normal commands within configured limits.
- **Vendor** – manufacturer or integrator. Can update firmware and configuration but cannot bypass safety laws.
- **Regulator** – authorised public body (e.g. safety agency). May impose additional constraints and demand logs.
- **Emergency Authority** – legally recognised emergency services (e.g. fire, ambulance, police) when configured.

Each role is represented in the system by an **authority token** (digital credential) that is verified before sensitive actions are executed.

---

## 3. Authority Tokens and Channels

HML assumes:

- **Authority tokens** (cryptographic credentials) bound to:
  - role (Owner / Guardian / Operator / Vendor / Regulator / Emergency Authority),
  - identity,
  - expiry and revocation status.
- **Command channels**:
  - local UI (e.g. screen, app, voice),
  - remote control interfaces (e.g. cloud dashboard, emergency link),
  - offline procedures (e.g. physical key + passcode) for minimal safe overrides.

Key rules:

1. High-risk tasks (e.g. moving heavy loads near people, financial transfers, surgical assistance) **require a valid token** for an appropriate role.
2. When no valid token is present, robots must:
   - treat input as **untrusted user** commands,
   - apply conservative rules (CHS/M or lower) and Failure Modes & Fallback Law.

---

## 4. Interaction with CHS Bands

The Human Mandate Layer and CHS ladder interact as follows:

- **CHS/UH (Blue)**:
  - high autonomy allowed **only** when a valid Owner / Operator token is active and context allows.
  - high-stakes tasks still require explicit confirmation from Owner, Guardian, or authorised Operator.
- **CHS/H (Green)**:
  - normal operations allowed with Operator tokens.
  - high-stakes tasks require Owner or Guardian confirmation.
- **CHS/M (Yellow)**:
  - assist-only; HML must downgrade all high-risk commands to suggestions.
  - any attempt to force irreversible actions MUST be blocked and logged.
- **CHS/L (Red)**:
  - safe-stop. HML must ignore all non-emergency commands.
  - only minimal commands that reduce risk (e.g. “confirm emergency call”) may be accepted, and even those can be rejected if unsafe.

If HML receives a command inconsistent with the current CHS band, it must:

1. Reject or downgrade the command.  
2. Record a receipt with `law_block_reason` referencing LEI = 1 and/or Failure Modes & Fallback Law.

---

## 5. Allowed and Blocked Overrides

### 5.1 Allowed Overrides (within law)

Examples of **allowed** actions when properly authorised:

- Owner changing operating modes (e.g. “night-only” operation) when ACS and TCS remain adequate.
- Guardian pausing the robot near children or infants.
- Regulator applying tighter speed or power limits.
- Emergency Authority requesting temporary priority for evacuation or fire-control tasks.

These actions may **tighten** constraints but must not weaken LEI = 1 or reduce coherence below configured thresholds.

### 5.2 Blocked Overrides (never allowed)

The following must ALWAYS be blocked, even with valid tokens:

- Commands that disable or bypass LEI = 1 or TQC.
- Commands that disable CHS monitoring or falsify ACS / TCS readings.
- Commands that order:
  - operation in unsafe environments that contradict Failure Modes & Fallback Law (e.g. deep water with untested hardware),
  - high-risk operations around infants when the law forbids them.
- Commands to erase or alter receipts or law logs.

For any blocked override, the robot or fleet must:

- remain in or move to a safe CHS band,
- create a TS-R receipt with role, token fingerprint, and `law_block_reason`.

---

## 6. Notifications and Escalation

HML defines a default notification ladder:

1. **Owner notification** – any CHS/L or law-block event MUST notify the Owner.
2. **Guardian notification** – if children / infants are present, Guardians MUST be notified of CHS/M or CHS/L.
3. **Vendor / Regulator notification** – for repeated law-blocks, repeated safe stops, or serious anomalies.
4. **Emergency services** – only when configured, and only for events that match local legal rules (e.g. gas leaks, fire, serious injury risk).

All notifications must be traceable via TS-R receipts.

---

## 7. TS-R1 vs TS-R2 Behaviour

- **TS-R1 (single robot)**:
  - applies HML rules directly to local commands and remote controls.
  - when multiple tokens are present, Owner > Guardian > Operator priority applies.
- **TS-R2 (swarm / fleet)**:
  - HML must enforce quorum rules for fleet-wide actions (e.g. two or more authorised humans for certain operations).
  - conflicting commands from different roles must be resolved conservatively (favour safety and higher-priority roles).

In all cases, Failure Modes & Fallback Law has precedence over convenience.

---

## 8. Receipt and Audit Requirements

Every high-risk action, override, or blocked command must:

- generate a TS-R receipt using TS-R Receipt Schema v1.0,
- include:
  - role and token fingerprint (pseudonymised where required by privacy law),
  - CHS band before and after,
  - relevant ACS and TCS values,
  - environment flags,
  - `law_block_reason` when applicable.

Auditors must be able to reconstruct:

- which human or institution authorised which action,
- whether HML correctly applied TruthSeal laws,
- whether the downgrade and notification behaviour matched TS-R Failure Modes & Fallback Law.

---

## 9. Compliance Checklist

A TS-R implementation is compliant with Human Mandate Layer v1.0 if:

1. All high-risk tasks require valid authority tokens.
2. CHS bands limit what authorised humans can request.
3. No token can disable or bypass LEI = 1, TQC, or CHS monitoring.
4. Children, infants, animals, water, and weather rules are enforced even against owner convenience.
5. All blocked or downgraded commands generate receipts with law references.
6. Swarm / fleet operations use quorum and conservative resolution for conflicting human commands.

If any of these conditions are not met, the system is **not compliant** with TS-R Human Mandate Layer v1.0.
