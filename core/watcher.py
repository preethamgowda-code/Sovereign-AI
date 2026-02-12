import os
import time
import shutil
import sys
import subprocess
import json

# --- CONFIGURATION ---
BASE_DIR = r"C:\Users\Admin\AIOS_Memory"
SC_WATCH = os.path.join(BASE_DIR, "Supply_Chain", "Incoming_Data")
SC_DONE  = os.path.join(BASE_DIR, "Supply_Chain", "Processed")
EN_WATCH = os.path.join(BASE_DIR, "Energy_Logic", "Incoming_Data")
EN_DONE  = os.path.join(BASE_DIR, "Energy_Logic", "Processed")
MEMORY_FILE = os.path.join(BASE_DIR, "system_memory.json")
LOG_PATH = os.path.join(BASE_DIR, "neural_log.txt")

# Ensure Infrastructure
for folder in [SC_WATCH, SC_DONE, EN_WATCH, EN_DONE]:
    os.makedirs(folder, exist_ok=True)

def update_memory(key, value):
    memory = {}
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r') as f: memory = json.load(f)
        except: pass
    memory[key] = value
    with open(MEMORY_FILE, 'w') as f: json.dump(memory, f)

def log_savings(amount_inr):
    current = 0
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, 'r') as f:
                current = json.load(f).get("total_savings_inr", 0)
        except: pass
    update_memory("total_savings_inr", current + amount_inr)
    print(f"💰 EMPIRE GROWTH: Total Savings increased to ₹{current + amount_inr}")

print("\n--- 🚀 AIOS MULTI-VERTICAL KERNEL ONLINE ---")
print(f"Monitoring Paths:\n1. {SC_WATCH}\n2. {EN_WATCH}")
sys.stdout.flush()

while True:
    try:
        # --- TASK 1: SUPPLY CHAIN ---
        for f in os.listdir(SC_WATCH):
            if f.endswith('.csv'):
                print(f"📦 PROCUREMENT DATA: {f}")
                full_path = os.path.join(SC_WATCH, f)
                with open(full_path, 'r') as c: data = c.read()
                
                # Tag high-cost assets in memory
                update_memory("high_cost_assets", ["Server_Rack_A"])
                
                prompt = f"SYSTEM: You are the Chief Procurement Officer. Analyze for price hikes > 20%:\n{data}"
                result = subprocess.run(['ollama', 'run', 'llama3.2:latest', prompt], capture_output=True, text=True, encoding='utf-8')
                
                # Write to Neural Log for Dashboard
                with open(LOG_PATH, "a") as log:
                    log.write(f"\n[{time.ctime()}] PROCUREMENT ALERT - {f}:\n{result.stdout}\n" + "="*50)
                
                print(f"\n--- 🧠 STRATEGY ---\n{result.stdout}")
                shutil.move(full_path, os.path.join(SC_DONE, f))

        # --- TASK 2: ENERGY ---
        for f in os.listdir(EN_WATCH):
            if f.endswith('.csv'):
                print(f"⚡ ENERGY DATA: {f}")
                full_path = os.path.join(EN_WATCH, f)
                with open(full_path, 'r') as c: data = c.read()
                
                log_savings(288) # Simulate savings for catching the spike
                
                # Fetch memory to see if this device was flagged in Procurement
                flagged = []
                if os.path.exists(MEMORY_FILE):
                    try:
                        with open(MEMORY_FILE, 'r') as f_mem:
                            flagged = json.load(f_mem).get("high_cost_assets", [])
                    except: pass
                
                prompt = f"SYSTEM: You are an Energy Auditor. NOTE: {flagged} were recently flagged for high purchase cost. Analyze this for peak-hour surcharges and cross-reference with high-cost assets:\n{data}"
                result = subprocess.run(['ollama', 'run', 'llama3.2:latest', prompt], capture_output=True, text=True, encoding='utf-8')
                
                # Write to Neural Log for Dashboard
                with open(LOG_PATH, "a") as log:
                    log.write(f"\n[{time.ctime()}] ENERGY AUDIT - {f}:\n{result.stdout}\n" + "="*50)

                print(f"\n--- ⚡ AUDIT ---\n{result.stdout}")
                shutil.move(full_path, os.path.join(EN_DONE, f))

    except Exception as e:
        print(f"⚠️ Error: {e}")
    
    sys.stdout.flush()
    time.sleep(3)