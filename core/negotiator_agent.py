import json
import os
import sys # Added to handle terminal encoding
from datetime import datetime

# 1. Define the Absolute Path
BASE_DIR = r"C:\Users\Admin\AIOS_Memory"
MEMORY_FILE = os.path.join(BASE_DIR, "system_memory.json")
LOG_FILE = os.path.join(BASE_DIR, "negotiation_log.txt")

def draft_negotiation_strategy(asset_id="Server_Rack_A"):
    if not os.path.exists(MEMORY_FILE):
        return f"Error: Memory file not found at {MEMORY_FILE}. Run the Watcher first."

    with open(MEMORY_FILE, 'r') as f:
        try:
            memory = json.load(f)
        except json.JSONDecodeError:
            return "Error: system_memory.json is empty or corrupted."
    
    savings = memory.get('total_savings_inr', 0)
    assets = memory.get('high_cost_assets', [])
    
    strategy = f"""
    --- AIOS EXECUTIVE NEGOTIATION BRIEF ---
    DATE: {datetime.now().strftime('%Y-%m-%d')}
    PRIMARY TARGET: {asset_id}
    DETECTED SYSTEM SAVINGS: INR {savings}
    
    LEVERAGE STRATEGY:
    1. AI Audit identified this asset as a core contributor to the INR {savings} inefficiency.
    2. Demand a performance-based rebate or technical audit from the vendor.
    3. Shift operation to off-peak hours to mitigate surcharge risks.
    """
    return strategy

# 2. Execution and Logging
if __name__ == "__main__":
    result = draft_negotiation_strategy()
    
    # Force UTF-8 encoding when writing to file to prevent future Unicode errors
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write(result)
    
    # Use a standard ASCII character instead of an emoji for the terminal
    print(f"SUCCESS: Negotiation brief generated at: {LOG_FILE}")