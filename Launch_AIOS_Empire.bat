@echo off
title Sovereign AI - Master Launch
color 0A
echo [SOVEREIGN AI] Starting Neural Kernel...
echo ---------------------------------------

:: 1. Start the Data Watcher
start "SOV_Watcher" cmd /k "cd /d C:\Users\Admin\AIOS_Memory && python core/watcher.py"

:: 2. Start the Negotiator Agent
start "SOV_Negotiator" cmd /k "cd /d C:\Users\Admin\AIOS_Memory && python core/negotiator_agent.py"

:: 3. Launch the Executive Dashboard (Direct Module Execution)
:: This uses the universal python -m syntax to ensure it finds the streamlit library
start "SOV_Dashboard" cmd /k "cd /d C:\Users\Admin\AIOS_Memory && python -m streamlit run interface/dashboard.py"

echo ---------------------------------------
echo [SUCCESS] If the dashboard doesn't open automatically, visit: http://localhost:8501
pause
