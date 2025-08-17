# 🏭 Digital Twin MVP – IoT Monitoring & Dashboard
A **proof-of-concept Digital Twin** that integrates **ESP32-based sensor hardware** with a **Python analytics pipeline** and **Streamlit dashboard**. The system simulates how industrial equipment can be monitored in real time, anomalies detected before failure, and insights visualized for operators.

## 📌 Table of Contents
1. Project Overview  
2. Objectives  
3. Architecture  
4. Tech Stack  
5. Folder Structure  
6. Setup Instructions  
7. Dashboard Preview  
8. Key Features  
9. Future Improvements  
10. About  

## 📖 Project Overview
Industrial systems often suffer downtime due to **late detection of issues** like overheating, high vibration, or abnormal current draw. This project demonstrates how a **Digital Twin** can:  
- Mirror real-world equipment with **live sensor data**  
- Provide **early warnings** through anomaly detection  
- Enable **data-driven decision-making** using an operator dashboard  

## 🎯 Objectives
- Collect **sensor data** (temperature, vibration, current) using ESP32  
- Log, clean, and analyze signals in **Python**  
- Apply **basic anomaly detection** to flag issues  
- Build a **Streamlit dashboard** for real-time visualization  

flowchart LR
    A[IoT Sensors<br>(Temp, Vibration)] --> B[ESP32<br>Data Logger]
    B --> C[Python Ingestion<br>(Serial/MQTT)]
    C --> D[Anomaly Detection<br>(Python, Pandas)]
    D --> E[Dashboard<br>(Streamlit)]


## 🛠️ Tech Stack
- **Hardware**: ESP32 microcontroller + DHT11/Current/Vibration sensors  
- **Firmware**: Arduino IDE (C++)  
- **Data Pipeline**: Python (pandas, NumPy)  
- **Anomaly Detection**: scikit-learn (Isolation Forest / Thresholding)  
- **Visualization**: Streamlit  
- **Version Control**: Git + GitHub  

## 📂 Folder Structure
```
digital-twin-mvp/
├─ firmware/                # ESP32 code
│  └─ esp32_logger.ino
│
├─ app/                     # Python backend
│  ├─ ingest.py             # Data ingestion from ESP32
│  ├─ analyze.py            # Anomaly detection logic
│  ├─ dashboard.py          # Streamlit dashboard
│  ├─ requirements.txt      # Python dependencies
│  └─ tests/                # Unit tests
│     └─ test_anomaly.py
│
├─ data/                    
│  └─ logs/                 # CSV logs from ESP32
│
└─ docs/                    
   └─ dashboard.png          # Dashboard preview
```

## ⚙️ Setup Instructions
### 1. Flash ESP32
- Open `firmware/esp32_logger.ino` in Arduino IDE  
- Select **ESP32 Dev Board** and upload firmware  

### 2. Install Python Dependencies
```bash
cd app
pip install -r requirements.txt
```

### 3. Run the Pipeline
```bash
# Start data ingestion
python ingest.py  

# Run anomaly detection
python analyze.py  

# Launch dashboard
streamlit run dashboard.py
```

### 4. Open Dashboard
Go to [http://localhost:8501](http://localhost:8501)  

## 📊 Dashboard Preview
![Dashboard Preview](docs/dashboard.png)  

KPIs displayed:  
- 🌡️ Temperature trend (°C)  
- 📈 Vibration intensity (g)  
- ⚡ Current draw (A)  
- 🟢 Sensor uptime & health  
- 🔴 Anomaly alerts (live)  

## ✨ Key Features
- Real-time sensor data ingestion from ESP32  
- CSV logging for reproducibility & analysis  
- Lightweight anomaly detection with scikit-learn  
- Interactive dashboard for operators  
- Extensible design for cloud/industrial integration  

## 🔮 Future Improvements
- Deploy dashboard using **Docker** for portability  
- Store data in **InfluxDB / PostgreSQL** for scalability  
- Use advanced **ML models** for predictive maintenance  
- Add cloud connectivity (AWS IoT / Azure IoT Hub)  
- Expand visualization with Grafana integration  

## 🙋 About
This project is part of my **learning portfolio** in IoT, Control Systems, and Digital Twins. It reflects my ability to combine **hardware (ESP32)** with **data analytics (Python)** and **visualization (Streamlit)** to solve real-world industrial challenges.
