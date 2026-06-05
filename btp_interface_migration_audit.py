#!/usr/bin/env python3
"""
Initiative 1: Middleware Consolidation & Cloud Integration
Script Name:  btp_interface_migration_audit.py
Objective:    Programmatically discover legacy point-to-point footprints, 
              quantify technical debt weight, calculate effort models, 
              and schedule date-centric migration waves.
Timeline:     Operationalized for June 2026 Landscape Rationalization Cycles.
"""

import json
import math
from datetime import datetime, timedelta

# Mock Database representing a live infrastructure metadata scan of an enterprise legacy middleware landscape
LEGACY_INTERFACES_INVENTORY = [
    {"id": "INT-091", "name": "Vendor_Master_Sync_PI", "type": "RFC", "custom_mapping_lines": 1250, "avg_payload_mb": 4.2, "criticality": "HIGH"},
    {"id": "INT-104", "name": "Customer_Invoice_Push_Neo", "type": "SOAP", "custom_mapping_lines": 450, "avg_payload_mb": 1.1, "criticality": "MEDIUM"},
    {"id": "INT-212", "name": "Legacy_Material_Fetch_TIBCO", "type": "IDOC", "custom_mapping_lines": 3200, "avg_payload_mb": 18.5, "criticality": "HIGH"},
    {"id": "INT-305", "name": "Employee_Onboarding_Boomi", "type": "REST", "custom_mapping_lines": 150, "avg_payload_mb": 0.5, "criticality": "LOW"},
    {"id": "INT-419", "name": "RealTime_Plant_Inventory_PO", "type": "RFC", "custom_mapping_lines": 890, "avg_payload_mb": 2.2, "criticality": "HIGH"},
    {"id": "INT-501", "name": "Deprecated_Tax_Calculator", "type": "SOAP", "custom_mapping_lines": 2100, "avg_payload_mb": 0.1, "criticality": "LOW"}
]

class TechnicalDebtAuditor:
    def __init__(self, inventory, base_date_str="2026-06-06"):
        """
        Initializes the technical debt discovery auditor with data points and timelines.
        """
        self.inventory = inventory
        self.base_date = datetime.strptime(base_date_str, "%Y-%m-%d")
        self.blended_engineering_rate = 75.00  # Global currency standard baseline ($/hour)
        
    def calculate_metrics(self, interface):
        """
        Implements the architectural complexity matrix calculation:
        Formula: CW = log10(Custom Mapping Lines) * Criticality Multiplier
        """
        lines = interface["custom_mapping_lines"]
        criticality_multiplier = 1.5 if interface["criticality"] == "HIGH" else 1.0
        
        # Calculate Complexity Weight (CW)
        complexity_weight = round(math.log10(lines) * criticality_multiplier, 2)
        
        # Calculate Effort Hours: Rule-of-thumb mapping baseline (4.5 hours per 100 lines adjusted by complexity)
        estimated_effort_hours = round((lines / 100) * 4.5 * complexity_weight, 1)
        
        # Financial baseline calculation (Cost of Delay / Migration Capital)
        cost_of_delay = round(estimated_effort_hours * self.blended_engineering_rate, 2)
        
        return complexity_weight, estimated_effort_hours, cost_of_delay

    def clean_core_rule_engine(self, interface, complexity_weight):
        """
        Deterministic decision rules mapping components to clean core parameters.
        """
        # Rule A: Low business value + legacy architecture footprint = Scheduled for deprecation
        if interface["criticality"] == "LOW" and interface["custom_mapping_lines"] > 1500:
            return "RETIRE / DECOMMISSION"
        
        # Rule B: High complexity weight or heavy coupling protocols = Requires Side-by-Side Cloud isolation
        elif complexity_weight > 4.0 or interface["type"] in ["RFC", "IDOC"]:
            return "SIDE-BY-SIDE (Cloud Integration Suite / Event Mesh)"
            
        # Rule C: Standard transactional flow with clean footprint = On-Stack via Stable Local APIs
        else:
            return "ON-STACK (Restricted Local API)"

    def generate_migration_roadmap(self):
        """
        Iterates over discovered assets to build an execution timeline roadmap.
        """
        print("==========================================================================================")
        print(f"ENTERPRISE INTERFACE MODERNIZATION & CLEAN CORE MIGRATION REPORT | RUN DATE: {self.base_date.strftime('%Y-%m-%d')}")
        print("==========================================================================================\n")
        
        total_reclaimed_hours = 0
        total_migration_cost = 0
        current_schedule_pointer = self.base_date
        
        print(f"{'ID':<8} {'Interface Descriptor':<30} {'Complexity':<12} {'Effort (Hrs)':<14} {'Target Wave Date':<18} {'Target Migration Vector'}")
        print("-" * 122)
        
        for item in self.inventory:
            complexity, effort_hours, cost_of_delay = self.calculate_metrics(item)
            target_vector = self.clean_core_rule_engine(item, complexity)
            
            # Date-eccentric task scheduling logic (assuming 8-hour delivery days per resource sprint)
            duration_days = max(int(effort_hours / 8), 1)
            target_wave_date = current_schedule_pointer + timedelta(days=duration_days)
            
            total_reclaimed_hours += effort_hours
            total_migration_cost += cost_of_delay
            
            print(f"{item['id']:<8} {item['name']:<30} {complexity:<12} {effort_hours:<14} {target_wave_date.strftime('%Y-%m-%d'):<18} {target_vector}")
            
            # Sequence downstream execution waves by padding dependencies with a 2-day stabilization buffer
            current_schedule_pointer = target_wave_date + timedelta(days=2) 
            
        print("-" * 122)
        print(f"📊 SYSTEMIC CONSOLIDATION SUMMARY:")
        print(f"  • Total Discovered Legacy Interfaces: {len(self.inventory)} Integration Flows")
        print(f"  • Total Landscape Refactoring Effort: {total_reclaimed_hours} Engineering Hours")
        print(f"  • Projected Modernization Asset Value: ${total_migration_cost:,.2f}")
        print(f"  • Complete Transition Horizon Target:  {current_schedule_pointer.strftime('%Y-%m-%d')}")
        print("==========================================================================================")

if __name__ == "__main__":
    # Execute the technical discovery audit tracking timeline constraints from June 2026
    auditor = TechnicalDebtAuditor(LEGACY_INTERFACES_INVENTORY, base_date_str="2026-06-06")
    auditor.generate_migration_roadmap()
