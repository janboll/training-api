from .test_fixtures import add_athlete_with_pb, client, client_data_to_dict


def test_empty_athlete(client):
    """ Tests the empty API response """
    rv = client.get("/api/athlete")
    assert b"[]\n" == rv.data


def test_athlete_with_pb(client, add_athlete_with_pb):
    """ Tests that a user and a PB have been created """
    rv = client.get("/api/athlete")
    athlete = client_data_to_dict(rv.data)
    assert len(athlete) == 1
    assert athlete[0]["age"] == 32
    assert athlete[0]["gender"] == "w"
    assert athlete[0]["vdot_value"] is None
    assert athlete[0]["weight"] == 60.0

    assert len(athlete[0]["personalbest"]) == 1

    rv = client.get(athlete[0]["personalbest"][0])
    pb = client_data_to_dict(rv.data)

    assert pb["athlete"] == 1
    assert pb["distance_in_meter"] == 1000
    assert pb["time_in_seconds"] == 50

