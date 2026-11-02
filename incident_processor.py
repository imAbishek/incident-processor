def filter_incidents(records, severity):
    result = []
    for incident in records:
        if incident["severity"] == severity:
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
