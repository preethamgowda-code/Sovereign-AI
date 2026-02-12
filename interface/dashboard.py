import streamlit as st
import json
import os
import pandas as pd
from fpdf import FPDF
from datetime import datetime

# 1. Initialize Page
st.set_page_config(page_title="AIOS Empire Dashboard", layout="wide")

# 2. Define Paths
BASE_DIR = r"C:\Users\Admin\AIOS_Memory"
MEMORY_FILE = os.path.join(BASE_DIR, "system_memory.json")
EN_DONE = os.path.join(BASE_DIR, "Energy_Logic", "Processed")
LOG_FILE = os.path.join(BASE_DIR, "neural_log.txt")

# 3. PDF Generation Function
def generate_pdf(savings, assets, history):
    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(200, 10, txt="AIOS EXECUTIVE AUDIT REPORT", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
    pdf.ln(10)

    # Summary Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="1. Financial Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Total System Savings: INR {savings}", ln=True)
    pdf.cell(200, 10, txt=f"Flagged High-Risk Assets: {', '.join(assets) if assets else 'None'}", ln=True)
    pdf.ln(5)

    # Audit Trail
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="2. Neural Decision History", ln=True)
    pdf.set_font("Arial", size=10)
    # Cleaning text for PDF encoding
    safe_history = history.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 5, txt=safe_history)
    
    return pdf.output(dest='S').encode('latin-1')

st.title("🚀 AIOS Empire Command Center")

# 4. Data Loading
data = {}
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'r') as f:
        try: data = json.load(f)
        except: data = {}

savings = data.get('total_savings_inr', 0)
assets = data.get('high_cost_assets', [])
history_text = ""
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        history_text = f.read()

# 5. Metrics Section
col1, col2, col3 = st.columns(3)
col1.metric("Total Savings", f"₹{savings}")
col2.metric("High-Risk Assets", len(assets))
col3.metric("Kernel Status", "ONLINE", delta="Optimal")

# 6. PDF DOWNLOAD BUTTON
st.divider()
if history_text:
    pdf_data = generate_pdf(savings, assets, history_text)
    st.download_button(
        label="📄 DOWNLOAD OFFICIAL PDF REPORT",
        data=pdf_data,
        file_name=f"AIOS_Audit_{datetime.now().strftime('%Y%m%d')}.pdf",
        mime="application/pdf"
    )
else:
    st.warning("⚠️ No Neural Log found. Process data in the Watcher to enable PDF export.")

# 7. Visual Analytics & History (Keep previous logic below)
st.subheader("📊 Energy Consumption Trends")
# ... [Keep your existing line_chart logic here] ...
st.divider()
st.subheader("📜 Neural Decision History")
st.text_area("Audit Trail", value=history_text, height=300)