import os

class SovereignAgent:
    """The standard blueprint for all agents running on the Sovereign Kernel."""
    
    def __init__(self, agent_name, vertical):
        self.name = agent_name
        self.vertical = vertical # e.g., 'Logistics', 'Finance', 'Health'
        self.log_path = r"C:\Users\Admin\AIOS_Memory\neural_log.txt"

    def emit_insight(self, message, savings=0):
        """Standardized method to talk to the Sovereign Shell & Neural Log."""
        entry = f"[{self.name.upper()}] | VERTICAL: {self.vertical} | {message}"
        if savings > 0:
            entry += f" | RECOVERED: ₹{savings}"
        
        with open(self.log_path, "a") as f:
            f.write(entry + "\n")
        print(f"🏛️ Sovereign Insight Emitted: {entry}")
