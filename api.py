from fastapi import FastAPI, HTTPException
from file_loader import load_incidents
from incident_processor import (
    filter_incidents,
    get_severity_count
)
from schemas import Incident, IncidentSummary

app = FastAPI()

def get_incidents():
    all_incidents = load_incidents("incidents.json")

    if all_incidents is None:
        raise HTTPException(status_code=500, detail="Unable to load incident data")

    return all_incidents

@app.get("/incidents/summary", response_model=IncidentSummary)
def incidents_summary():
    all_incidents = get_incidents()

    count_severity = get_severity_count(all_incidents)

    incident_summary = ({
        "total_incidents": len(all_incidents),
        "severity_count": count_severity,

    })
    return incident_summary

@app.get("/incidents")
def incidents(severity : str | None = None):
    all_incidents = get_incidents()

    if severity is not None:
        return filter_incidents(all_incidents, severity)

    return all_incidents

@app.post("/incidents")
def create_incident(incident: Incident):
    return incident