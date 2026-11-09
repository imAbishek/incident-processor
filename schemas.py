from pydantic import BaseModel

class Incident(BaseModel):
    id: int
    title: str
    severity: str
    status: str

class IncidentSummary(BaseModel):
    total_incidents : int
    severity_count : dict[str, int]

