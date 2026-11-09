from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_incidents():
    response = client.get("/incidents")
    assert response.status_code == 200
    incidents = response.json()
    assert len(incidents) == 5

def test_filer_high_severity():
    response = client.get(
        "/incidents",
        params={"severity": "high"}
    )
    assert response.status_code == 200
    incidents = response.json()
    assert len(incidents) == 2
    for incident in incidents:
        assert incident["severity"] == "high"

def test_post_valid_incidents():
    response = client.post(
        "/incidents",
        json={
            "id": 106,
            "title": "API timeout",
            "severity": "high",
            "status": "open"
        }
    )
    assert response.status_code == 200
    incidents = response.json()
    assert incidents.get("id") == 106
    assert incidents.get("status") == "open"

def test_post_invalid_incidents():
    response = client.post("/incidents", json={
        "id": 107,
        "title": "API timeout",
        "severity": "high",
    })
    assert response.status_code == 422
    errors = response.json()
    assert "detail" in errors
    for error in errors["detail"]:
        assert error["loc"] == ['body', 'status']