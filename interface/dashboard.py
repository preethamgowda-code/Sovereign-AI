import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime

# 1. Page Config & Professional Theme
st.set_page_config(page_title="Sovereign AI | Command", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a "Premium" Startup look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #238636; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. Path Logic
BASE_DIR = r"C:\Users\Admin\AIOS_Memory"
MEMORY_FILE = os.path.join(BASE_DIR, "system_memory.json")
LOG_FILE = os.path.join(BASE_DIR, "neural_log.txt")
NEGOTIATION_LOG = os.path.join(BASE_DIR, "negotiation_log.txt")

# 3. Data Loading
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'r') as f:
        data = json.load(f)
else:
    data = {"total_savings_inr": 0, "high_cost_assets": []}

savings = data.get('total_savings_inr', 0)
assets = data.get('high_cost_assets', [])

# 4. Header Section
st.title("🏛️ Sovereign AI: Executive Command")
st.caption(f"Kernel Status: ONLINE | Authorized User: Preetham Gowda | {datetime.now().strftime('%Y-%m-%d')}")
st.divider()

# 5. Metrics "The Big Three"
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("RECOVERABLE CAPITAL", f"₹{savings}", delta="Neural Audit Verified")
with col2:
    st.metric("HIGH-RISK ASSETS", len(assets), delta_color="inverse")
with col3:
    st.metric("SOVEREIGNTY SCORE", "100%", delta="Local-First")

# 6. Main Intelligence Feed
st.subheader("📜 Neural Audit Trail")
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        st.text_area("Live Kernel Reasoning", value=f.read(), height=250)
else:
    st.info("Waiting for Neural Kernel ingestion...")

st.divider()

# 7. PHASE 2: EXECUTIVE ACTION CENTER
st.subheader("🛠️ Autonomous Negotiation Center")
col_left, col_right = st.columns([1, 2])

with col_left:
    st.write("Convert audit findings into legal/commercial leverage.")
    if st.button("🚀 SYNTHESIZE NEGOTIATION BRIEF"):
        if os.path.exists(NEGOTIATION_LOG):
            with open(NEGOTIATION_LOG, 'r') as f:
                st.session_state['brief'] = f.read()
            st.success("Brief Synthesized.")
        else:
            st.error("Run negotiator_agent.py first.")

with col_right:
    if 'brief' in st.session_state:
        st.code(st.session_state['brief'], language="markdown")
        st.download_button("📩 Download Executive Brief", st.session_state['brief'], "Sovereign_Brief.txt")