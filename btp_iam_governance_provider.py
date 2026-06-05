#!/usr/bin/env python3
"""
Initiative 3: Automated BTP Cloud Security Governance
Script Name:  btp_iam_governance_provider.py
Objective:    Enforce programmatic Zero Trust security across cloud subaccounts. 
              Automatically audits identity access lifecycles, parses context signals, 
              and auto-revokes compromised or expired API keys/service accounts.
Timeline:     Operationalized for June 2026 Continuous Compliance Audits.
"""

import json
from datetime import datetime, timedelta

# Mock Database simulating active subaccount service accounts and non-human identity keys
ACTIVE_IAM_REGISTRY = [
    {"account_id": "SA-EXT-01", "app_name": "Logistics_Hyperscaler_Sync", "days_since_rotation": 14, "token_scope": "GLOBAL_ADMIN", "request_origin_region": "US-EAST"},
    {"account_id": "SA-EXT-02", "app_name": "Finance_Tax_Calculator_API", "days_since_rotation": 92, "token_scope": "READ_WRITE", "request_origin_region": "EU-CENTRAL"},
    {"account_id": "SA-EXT-03", "app_name": "Legacy_Warehouse_Middlware", "days_since_rotation": 185, "token_scope": "GLOBAL_ADMIN", "request_origin_region": "UNKNOWN"},
    {"account_id": "SA-EXT-04", "app_name": "Analytics_Data_Lake_Ingest", "days_since_rotation": 45, "token_scope": "READ_ONLY", "request_origin_region": "AP-SOUTH"},
    {"account_id": "SA-EXT-05", "app_name": "ThirdParty_Vendor_Portal", "days_since_rotation": 5, "token_scope": "WRITE_URGENT", "request_origin_region": "MALICIOUS_IP"}
]

class ZeroTrustGovernanceProvider:
    def __init__(self, iam_registry):
        self.registry = iam_registry
        self.audit_date = datetime.strptime("2026-06-06", "%Y-%m-%d")
        self.max_key_age_days = 90  # Corporate compliance rotation baseline rule
        
    def evaluate_security_risk(self, identity):
        """
        Evaluates real-time contextual signals to calculate systemic security risk levels.
        """
        risk_score = 0
        
        # Risk Vector 1: Key Rotation Staleness
        if identity["days_since_rotation"] > self.max_key_age_days:
            risk_score += 40
            
        # Risk Vector 2: Over-Privileged Scope Policy
        if identity["token_scope"] == "GLOBAL_ADMIN":
            risk_score += 30
            
        # Risk Vector 3: Anomalous Network Traffic Origin
        if identity["request_origin_region"] in ["UNKNOWN", "MALICIOUS_IP"]:
            risk_score += 50
            
        return risk_score

    def execute_governance_action(self, identity, risk_score):
        """
        Deterministic automated defense rules to enforce programmatic Least Privilege.
        """
        # Rule A: Critical threat detected -> Immediate active isolation and token revocation
        if identity["request_origin_region"] == "MALICIOUS_IP" or risk_score >= 80:
            return "🔴 ACTION: REVOKE IMMEDIATELY / BLOCK IDENTITY"
            
        # Rule B: Compliance policy breach (Stale Credentials) -> Automated Key Rotation Trigger
        elif identity["days_since_rotation"] > self.max_key_age_days:
            return "🟡 ACTION: FORCE KEY ROTATION / RESTRICT SCOPE"
            
        # Rule C: Secure compliant profile verified -> Authorize Access Standard session
        else:
            return "🟢 ACTION: AUTHORIZE / MAINTAIN PASSIVE MONITORING"

    def run_compliance_audit(self):
        print("==========================================================================================")
        print(f"ZERO TRUST ACCESS GOVERNANCE & INTERNALS COMPLIANCE DAEMON | RUN DATE: {self.audit_date.strftime('%Y-%m-%d')}")
        print("==========================================================================================\n")
        
        revoked_count = 0
        rotated_count = 0
        authorized_count = 0
        
        print(f"{'Identity ID':<13} {'Cloud Service Core Application':<30} {'Risk Score':<12} {'Compliance Verdict'}")
        print("-" * 122)
        
        for identity in self.registry:
            risk_score = self.evaluate_security_risk(identity)
            verdict = self.execute_governance_action(identity, risk_score)
            
            if "REVOKE" in verdict:
                revoked_count += 1
            elif "ROTATION" in verdict:
                rotated_count += 1
            else:
                authorized_count += 1
                
            print(f"{identity['account_id']:<13} {identity['app_name']:<30} {risk_score:<12} {verdict}")
            
        print("-" * 122)
        print("📊 AUDITABLE REGULATORY LIFECYCLE COMPLIANCE METRICS (SOX / GDPR / NIST):")
        print(f"  • Total Evaluated Non-Human Identities: {len(self.registry)} Active Service Accounts")
        print(f"  • Accounts Authorized (Safe Status)    : {authorized_count} Active Connections")
        print(f"  • Governance Rotations Triggered       : {rotated_count} Identities Forced")
        print(f"  • Active Automated Token Revocations    : {revoked_count} Critical Threats Extinguished")
        print(f"  • Automated Subaccount Security Index  : {round(((authorized_count + rotated_count) / len(self.registry)) * 100, 1)}% Compliant")
        print("==========================================================================================")

if __name__ == "__main__":
    governance_daemon = ZeroTrustGovernanceProvider(ACTIVE_IAM_REGISTRY)
    governance_daemon.run_compliance_audit()
