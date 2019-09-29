# TODO: replace with alembic data migration step
import requests
import time

import logging

logging.basicConfig(level=logging.DEBUG)


def send_data(endpoint, items):
    for item in items:
        resp = requests.request("POST", "http://localhost:5000/api/{}".format(endpoint), json=item)
        if resp.status_code != 201:
            print(resp.json())


tempos = [
    {
        "lower_percentage_hr": 70,
        "upper_percentage_hr": 75,
        "lower_percentage_max_vdot": 55,
        "upper_percentage_max_vdot": 65,
        "lower_seconds_per_km": 240,
        "upper_seconds_per_km": 300,
        "name": "long",
    }
]

trainingtypes = [
    {"type_name": "alternating"},
    {"type_name": "increasing"},
    {"type_name": "steady"}
]
trainings = [
    {"training_type_id": 3}
]

traininglaps = [
    {"training_id": 1, "lap": 1, "tempo": 1, "distance_in_meter": 10000}
]

if __name__ == "__main__":
    send_data("tempo", tempos)
    send_data("trainingtype", trainingtypes)
    send_data("training", trainings)
    send_data("traininglap", traininglaps)

