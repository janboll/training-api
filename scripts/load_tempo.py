# TODO: replace with alembic data migration step
import requests
import datetime

import logging

logging.basicConfig(level=logging.DEBUG)


def send_data(endpoint, items):
    for item in items:
        resp = requests.request("POST", "http://localhost:5000/api/{}".format(endpoint), json=item)
        if resp.status_code != 201:
            print(resp.json())


tempos = [
    {
        "lower_percentage_hr": 65,
        "upper_percentage_hr": 78,
        "lower_percentage_max_vdot": 59,
        "upper_percentage_max_vdot": 74,
        "name": "long",
    },
    {
        "lower_percentage_hr": 80,
        "upper_percentage_hr": 89,
        "lower_percentage_max_vdot": 75,
        "upper_percentage_max_vdot": 84,
        "name": "marathon",
    },
    {
        "lower_percentage_hr": 88,
        "upper_percentage_hr": 92,
        "lower_percentage_max_vdot": 83,
        "upper_percentage_max_vdot": 88,
        "name": "threshold",
    },
    {
        "lower_percentage_hr": 92,
        "upper_percentage_hr": 97,
        "lower_percentage_max_vdot": 89,
        "upper_percentage_max_vdot": 94,
        "name": "10k",
    },
    {
        "lower_percentage_hr": 97,
        "upper_percentage_hr": 100,
        "lower_percentage_max_vdot": 95,
        "upper_percentage_max_vdot": 100,
        "name": "intervall",
    },
    {
        "lower_percentage_hr": 100,
        "upper_percentage_hr": 100,
        "lower_percentage_max_vdot": 105,
        "upper_percentage_max_vdot": 120,
        "name": "repetitions",
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

trainingweek = [
    {"start_date": "2019-10-01", "athlete_id": "1"}
]

trainingweekschedule = [
    {"week_day": 0, "training_week_id": 1, "training_id": 1}
]

if __name__ == "__main__":
    send_data("tempo", tempos)
    send_data("trainingtype", trainingtypes)
    send_data("training", trainings)
    send_data("traininglap", traininglaps)
    send_data("trainingweek", trainingweek)
    send_data("trainingweekschedule", trainingweekschedule)

