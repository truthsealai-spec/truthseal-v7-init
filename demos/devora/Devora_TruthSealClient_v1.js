// ======================================================================
// DEVORA™ → TruthSeal™ Compliance Client (Frontend Helper)
// ======================================================================
//
// Purpose:
//   Thin React-friendly helper that calls a backend route which
//   1) builds the DEVORA context,
//   2) calls the TruthSeal Compliance Gateway,
//   3) returns the verdict + any saved dashboard data.
//
// IMPORTANT:
//   - This function calls YOUR backend (e.g. /api/devora/dashboard/save),
//     not the internal TruthSeal API directly (no API key in the browser).
//   - The backend route should use the TruthSeal_Compliance_Gateway_v1
//     and build_devora_dashboard_save_context().
//
// Usage in React (example):
//
//   import { saveDashboardWithCompliance } from './Devora_TruthSealClient_v1';
//
//   async function onSaveClick(dashboardPayload) {
//     try {
//       const result = await saveDashboardWithCompliance({
//         dashboardPayload,
//         environment: 'production',
//         isMultiTenant: true,
//         containsPii: true,
//         user: { id: currentUser.id, role: currentUser.role },
//       });
//       // result.allowed === true → show success
//     } catch (err) {
//       // Show error / verdict message to the user
//     }
//   }
//
// ======================================================================

/**
 * Call backend DEVORA save endpoint with TruthSeal compliance guard.
 *
 * @param {Object} params
 * @param {Object} params.dashboardPayload - Raw dashboard JSON from DEVORA UI.
 * @param {Object} params.user            - Current user ({ id, role }).
 * @param {string} params.environment     - "development" | "staging" | "production".
 * @param {boolean} params.isMultiTenant  - Whether this dashboard is in a multi-tenant env.
 * @param {boolean} params.containsPii    - Whether this dashboard touches PII-backed data.
 *
 * @returns {Promise<Object>} Parsed JSON from backend:
 *   {
 *     allowed: boolean,
 *     verdict: { ok, verdict, severity, details, metadata, ... },
 *     data?:   { ...savedDashboard }
 *   }
 */
export async function saveDashboardWithCompliance({
  dashboardPayload,
  user,
  environment,
  isMultiTenant,
  containsPii,
}) {
  const response = await fetch('/api/devora/dashboard/save-with-compliance', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      user,
      dashboardPayload,
      environment,
      is_multi_tenant: !!isMultiTenant,
      contains_pii: !!containsPii,
    }),
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const message =
      data.message ||
      data.error ||
      'DEVORA save blocked by TruthSeal compliance gateway.';
    throw new Error(message);
  }

  return data;
}
