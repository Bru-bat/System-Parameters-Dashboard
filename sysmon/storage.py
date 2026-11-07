import csv
from pathlib import Path
def append_data(path, row: dict) -> None:



    path = Path(path)
    path.parent.mkdir(parents = True, exist_ok = True)
    write_header = not path.exists() or path.stat().st_size == 0

    with open(path, 'a', newline = '') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = list(row.keys()))
        if write_header:
            writer.writeheader()
        writer.writerow(row)

    
if __name__ == "__main__":
    fake = {"cpu_usage": 10.0, "memory_used_percent": 50.0}
    append_data("data/test.csv", fake)
    append_data("data/test.csv", fake)