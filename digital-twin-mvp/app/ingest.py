# app/ingest.py
import os, json, time, pathlib
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
HOST = os.getenv("MQTT_HOST", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = os.getenv("MQTT_TOPIC", "plant/cnc01/telemetry")
LOG_DIR = pathlib.Path(os.getenv("LOG_DIR", "../data/logs"))
LOG_DIR.mkdir(parents=True, exist_ok=True)

def on_message(_client, _userdata, msg):
    ts = datetime.utcnow().isoformat()
    try:
        d = json.loads(msg.payload.decode())
        row = f'{ts},{d.get("ts")},{d.get("temp_c")},{d.get("vib_g")},{d.get("curr_a")}\n'
    except Exception:
        row = f'{ts},,,,\n'
    log_path = LOG_DIR / (datetime.utcnow().strftime("%Y%m%d") + ".csv")
    new = not log_path.exists()
    with open(log_path, "a") as f:
        if new:
            f.write("iso_ts,device_ts,temp_c,vib_g,curr_a\n")
        f.write(row)

def main():
    c = mqtt.Client()
    c.on_message = on_message
    c.connect(HOST, PORT, 60)
    c.subscribe(TOPIC, qos=0)
    print(f"[ingest] Subscribed {TOPIC} @ {HOST}:{PORT}; writing to {LOG_DIR}")
    c.loop_forever()

if __name__ == "__main__":
    main()
