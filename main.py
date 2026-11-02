from incident_processor import (
    validate_all_fields,
    filter_incidents,
    get_missing_fields,
)
from file_loader import load_incidents

incidents = load_incidents("incidents.json")

print("=== Incident Data Processor ===")

if incidents is not None:
    print(len(incidents))

    result = validate_all_fields(incidents)
    valid_incidents = []

    if result:
        for incident in result:
            print(f"Incident: {incident['id']} | Missing Fields: {incident['missing_fields']}")

    else:
        print("All incidents are valid")

    for incident in incidents:
        missing_fields = get_missing_fields(incident)
        if missing_fields:
            continue
        else:
            valid_incidents.append(incident)

    high_severity =  filter_incidents(valid_incidents, "high")

    if high_severity:
        print("=== High Severity Data Processor ===")
        for incident in high_severity:
            print(f"ID: {incident['id']} | {incident['title']}")
    else:
        print("No high severity incidents found")
else:
    print("Cannot process incidents")



