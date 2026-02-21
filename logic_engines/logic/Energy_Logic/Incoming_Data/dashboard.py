import streamlit as st
import json
import os
import pandas as pd

st.set_page_config(page_title="AIOS Dashboard", layout="wide")

MEMORY_FILE = r"C:\Users\Admin\AIOS_Memory\system_memory.json"

st.title("🚀 AIOS Empire Command Center")

# --- TOP METRICS ---
col1, col2, col3 = st.columns(3)

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'r') as f:
        data = json.load(f)
        
    with col1:
        st.metric("Total Savings", f"₹{data.get('total_savings_inr', 0)}")
    with col2:
        st.metric("High-Risk Assets", len(data.get('high_cost_assets', [])))
    with col3:
        st.metric("Kernel Status", "ONLINE", delta="Optimal")

st.divider()

# --- RECENT ACTIVITY ---
st.subheader("Latest Neural Insights")
# This pulls the last 5 lines from a log or just shows the memory
st.write("Current High-Cost Watchlist:", data.get('high_cost_assets', []))

st.info("💡 Recommendation: Shift Server_Rack_A workloads to 11:00 PM to maximize savings.")