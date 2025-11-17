// ======================================================================
// DEVORA™ Dashboard Demo with TruthSeal™ Sovereign Status Line
// ======================================================================
//
// Purpose:
//   Tiny React demo component that:
//     1) Calls the existing DEVORA → TruthSeal client helper
//     2) Shows a small status line when compliance passes:
//            "(Sovereign Devora Activated)"
//
// Notes:
//   - This is a UI demo only; replace the placeholder dashboardPayload,
//     user, and flags with real values when integrating into DEVORA.
//   - The status line only appears when the TruthSeal verdict allows
//     the save (result.allowed === true).
// ======================================================================

import React, { useState } from "react";
import { saveDashboardWithCompliance } from "./Devora_TruthSealClient_v1";

export function Devora_SovereignStatusDemo_v1() {
  const [isSaving, setIsSaving] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [sovereignActive, setSovereignActive] = useState(false);

  async function handleSaveClick() {
    setIsSaving(true);
    setErrorMessage(null);

    try {
      // ------------------------------------------------------------------
      // Placeholder payload: replace with real DEVORA dashboard data.
      // ------------------------------------------------------------------
      const result = await saveDashboardWithCompliance({
        dashboardPayload: {
          id: "demo-dashboard-001",
          name: "DEVORA Sovereign Demo",
        },
        environment: "production",
        isMultiTenant: true,
        containsPii: true,
        user: {
          id: "devora_demo_user",
          role: "dashboard_designer",
        },
      });

      // Expecting the helper to return:
      // { allowed: boolean, verdict: { ok, code, severity, details, ... } }
      if (result && result.allowed) {
        setSovereignActive(true);
      } else {
        setSovereignActive(false);
        const details =
          result?.verdict?.details ||
          result?.verdict?.code ||
          "Save blocked by TruthSeal™ policy.";
        setErrorMessage(details);
      }
    } catch (err: any) {
      setSovereignActive(false);
      setErrorMessage(err?.message || "Unexpected error during save.");
    } finally {
      setIsSaving(false);
    }
  }

  return (
    <div style={{ padding: 16, fontFamily: "system-ui, -apple-system, sans-serif" }}>
      <h3 style={{ marginTop: 0 }}>DEVORA™ Sovereign Save Demo</h3>

      <button
        onClick={handleSaveClick}
        disabled={isSaving}
        style={{
          padding: "8px 14px",
          fontSize: 14,
          cursor: isSaving ? "default" : "pointer",
        }}
      >
        {isSaving ? "Saving…" : "Save DEVORA Dashboard"}
      </button>

      {errorMessage && (
        <div
          style={{
            marginTop: 8,
            fontSize: 12,
            color: "#cc0000",
          }}
        >
          {errorMessage}
        </div>
      )}

      {sovereignActive && !errorMessage && (
        <div
          style={{
            marginTop: 8,
            fontSize: 12,
            opacity: 0.8,
          }}
        >
          (Sovereign Devora Activated)
        </div>
      )}
    </div>
  );
}

export default Devora_SovereignStatusDemo_v1;
