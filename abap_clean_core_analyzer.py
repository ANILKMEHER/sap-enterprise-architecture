#!/usr/bin/env python3
"""
Initiative 2: Clean Core Assessment & Cloud Application Models
Script Name:  abap_clean_core_analyzer.py
Objective:    Programmatically parse custom object metadata, evaluate direct database 
              coupling weights, detect Clean Core violations, and calculate refactoring 
              estimates for cloud-native side-by-side migration.
Timeline:     Operationalized for June 2026 Code Rationalization Frameworks.
"""

import json
from datetime import datetime

# Mock Metadata representing a custom repository object scan of an enterprise core system
CUSTOM_OBJECTS_BACKLOG = [
    {"object_name": "ZCL_VENDOR_RECONCILE", "type": "CLASS", "lines_of_code": 1850, "direct_db_selects": 42, "unreleased_api_calls": 12, "criticality": "HIGH"},
    {"object_name": "ZREPORT_INVENTORY_VAL", "type": "REPORT", "lines_of_code": 3200, "direct_db_selects": 85, "unreleased_api_calls": 25, "criticality": "HIGH"},
    {"object_name": "ZTM_ENHANCE_SHIPMENT", "type": "BADI", "lines_of_code": 350, "direct_db_selects": 4, "unreleased_api_calls": 1, "criticality": "MEDIUM"},
    {"object_name": "ZFUNC_TAX_CALC_OLD", "type": "FUNCTION", "lines_of_code": 920, "direct_db_selects": 0, "unreleased_api_calls": 0, "criticality": "LOW"},
    {"object_name": "ZCL_CUSTOMER_OVP_EXT", "type": "CLASS", "lines_of_code": 710, "direct_db_selects": 15, "unreleased_api_calls": 2, "criticality": "MEDIUM"}
]

class CleanCoreAnalyzer:
    def __init__(self, objects_backlog):
        self.backlog = objects_backlog
        self.remediations_run_date = "2026-06-06"
        
    def score_technical_debt(self, obj):
        """
        Quantifies architectural coupling and technical debt weight.
        Formula: Debt Score = (Lines of Code / 100) + (Direct DB Selects * 2) + (Unreleased API Calls * 5)
        """
        loc_weight = obj["lines_of_code"] / 100
        db_weight = obj["direct_db_selects"] * 2
        api_violation_weight = obj["unreleased_api_calls"] * 5
        
        debt_score = round(loc_weight + db_weight + api_violation_weight, 2)
        
        # Calculate refactoring hours based on debt score severity and criticality
        multiplier = 2.5 if obj["criticality"] == "HIGH" else 1.5
        refactor_hours = round(debt_score * multiplier, 1)
        
        return debt_score, refactor_hours

    def evaluate_clean_core_vector(self, obj, debt_score):
        """
        Deterministic extensibility strategy rules based on architectural coupling severity.
        """
        # Rule 1: Low criticality, zero dependencies, legacy object -> Retrenchment
        if obj["criticality"] == "LOW" and obj["direct_db_selects"] == 0:
            return "RETIRE / DECOMMISSION"
            
        # Rule 2: High DB coupling or heavy legacy violation scores -> Isolate to Side-by-Side Cloud Platform
        elif debt_score > 50.0 or obj["unreleased_api_calls"] > 10:
            return "SIDE-BY-SIDE (CAPM / RAP Cloud-Native Runtime)"
            
        # Rule 3: Moderate footprint -> Move to On-Stack Developer Extensibility (Stable Local APIs)
        else:
            return "ON-STACK EXTENSIBILITY (Restricted Local ABAP Core)"

    def execute_static_analysis(self):
        print("==========================================================================================")
        print(f"ABAP CLEAN CORE ARCHITECTURE ASSESSMENT & STATIC ANALYSIS RUN | DATE: {self.remediations_run_date}")
        print("==========================================================================================\n")
        
        total_objects = len(self.backlog)
        side_by_side_count = 0
        on_stack_count = 0
        retired_count = 0
        accumulated_refactor_hours = 0
        
        print(f"{'Object Identifier':<23} {'Type':<10} {'Debt Score':<12} {'Refactor Hrs':<14} {'Target Extensibility Vector'}")
        print("-" * 122)
        
        for obj in self.backlog:
            debt_score, refactor_hours = self.score_technical_debt(obj)
            vector = self.evaluate_clean_core_vector(obj, debt_score)
            accumulated_refactor_hours += refactor_hours
            
            if "SIDE-BY-SIDE" in vector:
                side_by_side_count += 1
            elif "ON-STACK" in vector:
                on_stack_count += 1
            else:
                retired_count += 1
                
            print(f"{obj['object_name']:<23} {obj['type']:<10} {debt_score:<12} {refactor_hours:<14} {vector}")
            
        print("-" * 122)
        print("📊 AGGREGATED EXTENSIBILITY DISTRIBUTION METRICS:")
        print(f"  • Total Scanned Repository Custom Objects     : {total_objects}")
        print(f"  • Side-by-Side Cloud Modernization Targets    : {side_by_side_count} Objects ({round((side_by_side_count/total_objects)*100, 1)}%)")
        print(f"  • On-Stack Upgrade-Safe Adaptation Targets   : {on_stack_count} Objects ({round((on_stack_count/total_objects)*100, 1)}%)")
        print(f"  • Legacy Assets Identified for Decommission   : {retired_count} Objects ({round((retired_count/total_objects)*100, 1)}%)")
        print(f"  • Total Project Modernization Backlog Velocity: {accumulated_refactor_hours} Engineering Hours")
        print("==========================================================================================")

if __name__ == "__main__":
    analyzer = CleanCoreAnalyzer(CUSTOM_OBJECTS_BACKLOG)
    analyzer.execute_static_analysis()
