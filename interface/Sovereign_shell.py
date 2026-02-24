import time
from core.manager_agent import SovereignManager
from core.report_generator import SovereignReportGenerator
from logic_engines.health_watcher import HealthWatcher

class SovereignShell:
    def __init__(self):
        # Initializing the brain of the operation
        self.manager = SovereignManager(memory_client=None) 
        self.reporter = SovereignReportGenerator()
        self.health = HealthWatcher()

    def trigger_full_audit(self):
        print("🏛️ [Sovereign Shell] Initiating Cross-Vertical Scan...")
        
        # Simulated local telemetry for the Healthcare vertical
        health_data = [{"item": "MRI Helium", "days_to_expiry": 3, "value": 50000}]
        
        # Step 1: Execute Vertical Audits
        health_insights = [self.health.audit_inventory(health_data)]
        
        # Step 2: Orchestrate via Manager for ROI Prioritization
        top_insight = self.manager.consolidate_insights(health_insights, [], [])
        
        # Step 3: Local Document Generation
        if top_insight:
            report_path = self.reporter.generate_capital_recovery_report([top_insight])
            print(f"✨ Audit Success. Recovered: ₹{top_insight['savings']}")
            return report_path