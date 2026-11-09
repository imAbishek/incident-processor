import pytest
from schemas import Incident
from pydantic import ValidationError

def test_incident_missing_status():
    with pytest.raises(ValidationError) as e:
        Incident.model_validate({
            'id': 101,
            'title': 'Missing Status',
            'severity': 'medium',
        })
    assert e.value.errors()[0]['loc'] == ('status',)

def test_valid_incident():
    incident = {
        'id': 101,
        'title': 'Missing Status',
        'severity': 'medium',
        'status': 'open'
    }
    validated = Incident.model_validate(incident)

    assert validated.id == 101
    assert validated.status == 'open'







