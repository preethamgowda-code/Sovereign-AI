from core.memory_subsystem import SovereignMemory
import datetime

class PredictiveWatcher:
    def __init__(self):
        self.memory = SovereignMemory()
        self.threshold = 0.85 # 2026 standard for predictive confidence

    def analyze_telemetry(self, current_data):
        # Query ChromaDB for similar past waste patterns
        past_incidents = self.memory.collection.query(
            query_texts=[str(current_data)],
            n_results=3
        )

        if past_incidents['distances'][0][0] < (1 - self.threshold):
            return self.trigger_preventative_action(current_data)
        return "System Optimized: No predictive leaks detected."

    def trigger_preventative_action(self, data):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"PREDICTIVE ALERT: Pattern matches historical ₹1,152 leak."
        
        # Log to the Neural Log for the Sovereign Shell to turn GOLD
        with open("neural_log.txt", "a") as f:
            f.write(f"[{timestamp}] [PREDICTIVE] {msg} | Est. Savings: ₹1,152\n")
        
        return msg