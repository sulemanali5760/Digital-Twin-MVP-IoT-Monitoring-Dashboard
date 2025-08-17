# app/tests/test_anomaly.py
import pandas as pd
from analyze import compute

def test_flags_trigger():
    df = pd.DataFrame({
        "iso_ts":["2024-01-01T00:00:00Z"]*5,
        "device_ts":[0,1,2,3,4],
        "temp_c":[30,31,45,31,30],   # 45 triggers critical
        "vib_g":[0.2,0.3,0.9,0.2,0.2], # 0.9 triggers critical
        "curr_a":[3.5,3.8,5.2,3.6,3.5] # 5.2 triggers critical
    })
    out = compute(df)
    assert (out["severity"].max() == 2)
