import time
from datetime import datetime

from sysmon.collector import collect
from sysmon.storage import append_data

INTERVAL_SECONDS = 5
CSV_PATH = "data/pc_data.csv"

def run() -> None:
    try:
        while True:
            start = time.monotonic()
            row = {}
            data = collect()  # 1. collect
            row = {"timestamp": datetime.now().isoformat(timespec="seconds"), **data} # 2. add timestamp
            try:
                append_data(CSV_PATH, row)  # 3. store
            except PermissionError:
                print("Logging error")
            stop = time.monotonic() - start
            time.sleep(INTERVAL_SECONDS - stop)  # 4. wait
    except KeyboardInterrupt:
        print("Logger Stopped")

if __name__ == "__main__":
    run()