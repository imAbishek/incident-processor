from incident_processor import (
    get_missing_fields,
    validate_all_fields,
    filter_incidents,
    get_severity_count
)

def test_missing_fields():
    incident = {
        "id": 201,
        "title": "Database unavailable",
        "severity": "high"
    }

    missing = get_missing_fields(incident)

    assert missing == ["status"]

    print("Missing-field test passed")


def test_batch_validation():
    incidents = [
        {
            "id": 301,
            "title": "API unavailable",
            "severity": "high",
            "status": "open"
        },
        {
            "id": 302,
            "title": "Database slow",
            "severity": "medium"
        }
    ]
    errors = validate_all_fields(incidents)
    assert len(errors) == 1
    assert errors[0]['id'] == 302
    assert errors[0]['missing_fields'] == ['status']

    print("Batch-validation test passed")


def test_severity_filtering():
    incidents = [
        {"id": 401, "severity": "high"},
        {"id": 402, "severity": "low"},
        {"id": 403, "severity": "high"}
    ]

    result = filter_incidents(incidents, "high")
    assert len(result) == 2
    assert result[0]['id'] == 401
    assert result[1]['id'] == 403
    ids = [incident['id'] for incident in result]
    assert 402 not in ids
    print("Severity filtering test passed")

def test_get_severity_count():
    incidents = [
        {"id": 401, "severity": "high"},
        {"id": 402, "severity": "high"},
        {"id": 403, "severity": "high"},
        {"id": 404},
    ]

    result = get_severity_count(incidents)
    assert result == {"high": 3}
    print("Severity count test passed")


if __name__ == "__main__":
    test_missing_fields()
    test_batch_validation()
    test_severity_filtering()