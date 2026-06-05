# Initiative 2: Clean Core Assessment & Cloud Application Models Runbook 📉

## 📋 Executive Overview & Strategic Intent
Modifying the stable base layer of core enterprise application software packages blocks an organization's upgrade velocity and halts technological agility. This strategy establishes an analytical auditing framework to inspect custom repository objects, measure database call weights, and programmatically determine if an asset should be retired, adapted locally, or refactored side-by-side using robust cloud application models.

---

## 📊 Clean Core Prioritization Framework

Custom system setups are systematically classified based on their total dependency weight and potential risk parameters.

| Architectural Indicator | Code Metric Base | Target Modernization Vector |
| :--- | :--- | :--- |
| **Low Criticality / High Debt** | Zero active system calls or dependencies. | **Retire & Decommission** |
| **Standard Core Operations** | Low complexity, standard data modifications. | **On-Stack Extensibility** via Released APIs. |
| **High Scale / Complex Customization** | Extreme database reads or unreleased core calls. | **Side-by-Side App** on Cloud Runtimes. |

---

## 💻 Python Automation Engine
*The following static code analysis utility evaluates custom objects against database layer weights and outputs a clear cloud-extensibility roadmap.*

```python
#!/usr/bin/env python3
import json

CUSTOM_OBJECTS_BACKLOG = [
    {"object_name": "ZCL_VENDOR_RECONCILE", "type": "CLASS", "lines_of_code": 1850, "direct_db_selects": 42, "unreleased_api_calls": 12, "criticality": "HIGH"},
    {"object_name": "ZREPORT_INVENTORY_VAL", "type": "REPORT", "lines_of_code": 3200, "direct_db_selects": 85, "unreleased_api_calls": 25, "criticality": "HIGH"},
    {"object_name": "ZTM_ENHANCE_SHIPMENT", "type": "BADI", "lines_of_code": 350, "direct_db_selects": 4, "unreleased_api_calls": 1, "criticality": "MEDIUM"},
    {"object_name": "ZFUNC_TAX_CALC_OLD", "type": "FUNCTION", "lines_of_code": 920, "direct_db_selects": 0, "unreleased_api_calls": 0, "criticality": "LOW"}
]

class CleanCoreAnalyzer:
    def __init__(self, objects_backlog):
        self.backlog = objects_backlog
        
    def score_technical_debt(self, obj):
        loc_weight = obj["lines_of_code"] / 100
        db_weight = obj["direct_db_selects"] * 2
        api_violation_weight = obj["unreleased_api_calls"] * 5
        debt_score = round(loc_weight + db_weight + api_violation_weight, 2)
        refactor_hours = round(debt_score * (2.5 if obj["criticality"] == "HIGH" else 1.5), 1)
        return debt_score, refactor_hours

    def evaluate_clean_core_vector(self, obj, debt_score):
        if obj["criticality"] == "LOW" and obj["direct_db_selects"] == 0:
            return "RETIRE / DECOMMISSION"
        elif debt_score > 50.0 or obj["unreleased_api_calls"] > 10:
            return "SIDE-BY-SIDE (CAPM / RAP Cloud-Native Runtime)"
        else:
            return "ON-STACK EXTENSIBILITY (Restricted Local Core)"

    def execute_static_analysis(self):
        for obj in self.backlog:
            score, hours = self.score_technical_debt(obj)
            vector = self.evaluate_clean_core_vector(obj, score)
            print(f"Object: {obj['object_name']} | Debt: {score} | Vector: {vector}")

if __name__ == "__main__":
    analyzer = CleanCoreAnalyzer(CUSTOM_OBJECTS_BACKLOG)
    analyzer.execute_static_analysis()
