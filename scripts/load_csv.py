from scripts.load_tempo import send_data

from csv import reader
from datetime import datetime, timedelta

distances=[1000, 1500, 3000, 5000, 10000, 15000, 21097, 25000, 42195]

with open("vdot.csv") as csvfile:
    vdotreader = reader(csvfile, delimiter='\t', )
    for line in vdotreader:
        if line[0] == "VDOT":
            continue
        items = []
        for i, time_string in enumerate(line[1:]):
            if time_string[0] != "-":
                if len(time_string.split(":")) == 2:
                    format = "%M:%S"
                else:
                    format = "%H:%M:%S"
                t = datetime.strptime(time_string.strip(), format)
                delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                items.append({
                    "vdot": float(line[0]),
                    "distance_in_meter": int(distances[i]),
                    "time_in_seconds": int(delta.total_seconds())
                })
        send_data("vdot", items)

