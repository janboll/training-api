from scripts.load_tempo import send_data

from csv import reader
from datetime import datetime, timedelta

distances=[1000, 1500, 3000, 5000, 10000, 15000, 21097, 25000, 42195]

def load_vdot():
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


def _create_tempo(vdot, tempo, pace_in_seconds, distance_in_meter=None):
    return {
        "vdot": vdot,
        "tempo": tempo,
        "pace_in_seconds_per_km": pace_in_seconds,
    }


def _load_pace_in_min(timestring):
    t = datetime.strptime(timestring.strip(), "%M:%S")
    delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    return delta.total_seconds()


def load_tempo():
    with open("tempo.csv") as csvfile:
        temporeader = reader(csvfile, delimiter=" ")
        for line in temporeader:
            if line[0] == "VDOT":
                continue
            items = []
            vdot = line[0]
            items.append(_create_tempo(vdot, 1, _load_pace_in_min(line[1])))
            items.append(_create_tempo(vdot, 2, _load_pace_in_min(line[2])))
            send_data("vdot_tempo", items)


#load_vdot()
load_tempo()