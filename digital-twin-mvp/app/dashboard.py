# app/dashboard.py
import os, time, pathlib, pandas as pd, streamlit as st
from dotenv import load_dotenv
from analyze import compute, latest_csv

st.set_page_config(page_title="IoT Digital Twin Dashboard", layout="wide")
st.title("IoT Monitoring Dashboard")

load_dotenv()
refresh = st.sidebar.slider("Auto-refresh (sec)", 2, 30, 5)

placeholder = st.empty()
while True:
    try:
        df = pd.read_csv(latest_csv())
        df = compute(df)
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        uptime = 96.7  # demo KPI
        energy_saving = 8.0
        lead_time_hr = 2.5
        coverage = 87

        kpi1.metric("System Uptime", f"{uptime:.1f}%")
        kpi2.metric("Energy Savings (vs prev.)", f"{energy_saving:.0f}%")
        kpi3.metric("Fault Lead Time", f"{lead_time_hr:.1f} h")
        kpi4.metric("Sensor Coverage", f"{coverage}%")

        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Temperature (°C)")
            st.line_chart(df.set_index("iso_ts")[["temp_c","temp_c_avg"]])
            st.caption("Yellow = warning, Red = critical")
        with c2:
            st.subheader("Vibration (g)")
            st.line_chart(df.set_index("iso_ts")[["vib_g","vib_g_avg"]])

        c3, c4 = st.columns(2)
        with c3:
            st.subheader("Current (A)")
            st.line_chart(df.set_index("iso_ts")[["curr_a","curr_a_avg"]])
        with c4:
            st.subheader("Severity (0=OK,1=Warn,2=Crit)")
            st.area_chart(df.set_index("iso_ts")[["severity"]])

        st.caption("Live data from MQTT via ESP32 → CSV log → analysis → KPIs.")
    except Exception as e:
        st.warning(f"Waiting for data… ({e})")
    time.sleep(refresh)
