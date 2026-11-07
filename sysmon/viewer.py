import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def data_viewer(path) -> None:
    path = Path(path)
    path.parent.mkdir(parents = True, exist_ok = True)
    df = pd.read_csv(path, parse_dates = ["timestamp"])
    df.set_index("timestamp")
    axes = df[["cpu_usage", "cpu_frequency_current"]].plot(title = "CPU Usage", subplots = True, grid = True)
    units = ["CPU usage [%]", "CPU frequency [MHz]"]
    for axes, label in zip(axes, units):
        axes.set_ylabel(label)
        axes.set_xlabel("Time")
    plt.show()

if __name__ == "__main__":
    data_viewer("data/pc_data.csv")
