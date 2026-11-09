def filter_incidents(records, severity):
    result = []
    for incident in records:
        if incident.get('severity') == severity:
            result.append(incident)
    return result


def get_missing_fields(incident : dict) -> list[str]:
    required_fields = ["id", "title", "severity", "status"]
    missing_fields = []

    for field in required_fields:
        if field not in incident:
            missing_fields.append(field)

    return missing_fields

def validate_all_fields(records):
    errors = []

    for incident in records:
        missing_fields = get_missing_fields(incident)
        if missing_fields:
            errors.append({
                "id": incident.get("id", "unknown"),
                "missing_fields": missing_fields
            })
    return errors

def get_valid_incidents(records: list[dict]) -> list[dict]:
    valid_incidents = []

    for incident in records:
        missing_fields = get_missing_fields(incident)
        if missing_fields:
            continue
        else:
            valid_incidents.append(incident)

    return valid_incidents

def get_severity_count(records: list[dict]) -> dict[str, int]:
    count_severity = {}
    for incident in records:
        if incident.get('severity') is not None:
            count_severity[incident["severity"]] = count_severity.get(incident['severity'], 0) + 1

    return count_severity
