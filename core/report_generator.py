import datetime

class SovereignReportGenerator:
    def __init__(self, output_dir="reports/"):
        self.output_dir = output_dir

    def generate_capital_recovery_report(self, prioritized_insights):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"{self.output_dir}Sovereign_Audit_{timestamp}.txt"
        
        total_recovery = sum(item['savings'] for item in prioritized_insights)
        
        report_content = [
            "🏛️ SOVEREIGN AI: CAPITAL RECOVERY EXECUTIVE AUDIT",
            f"Generated: {datetime.datetime.now()}",
            "Status: LOCAL-FIRST (Zero Data Egress)",
            "="*50,
            f"TOTAL IDENTIFIED RECOVERY: ₹{total_recovery}",
            "="*50,
            "\nVERTICAL BREAKDOWN:"
        ]
        
        for insight in prioritized_insights:
            report_content.append(f"- [{insight['vertical']}] {insight['message']} | Potential: ₹{insight['savings']}")
            
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(report_content))
            
        print(f"✅ Executive Audit Generated: {filename}")
        return filename