# Incident Data Processor

A Python-based incident processing application with a **CLI and FastAPI REST API**. It loads incident records from JSON, validates data, filters incidents by severity, and generates summary statistics.

Built as a hands-on backend engineering project covering Python, FastAPI, Pydantic, HTTP handling, and automated testing.

## Features

- **Incident Processing:** Load JSON records, detect missing fields, filter by severity, and calculate severity counts.
- **CLI:** Process incidents locally and display validation errors and high-severity incidents.
- **REST API:** Retrieve incidents, filter by severity, view summaries, and validate submitted incident data.
- **Pydantic Validation:** Validate request bodies and enforce response schemas.
- **Error Handling:** Handle file errors, malformed JSON, HTTP failures, timeouts, and invalid API requests.
- **Automated Testing:** 10 pytest tests covering incident processing, API endpoints, and Pydantic validation.

## Tech Stack

Python 3.11+ · FastAPI · Pydantic · pytest · HTTPX · Requests

## Project Structure

```text
incident-processor/
├── api.py                 # FastAPI endpoints
├── schemas.py             # Pydantic models
├── main.py                # CLI entry point
├── incident_processor.py  # Processing and validation logic
├── file_loader.py         # JSON loading and error handling
├── api_client.py          # Standalone HTTP client example
├── incidents.json         # Sample incident data
├── test_api.py            # API endpoint tests
├── test_processor.py      # Processing tests
├── test_schemas.py        # Pydantic validation tests
├── slow_server.py         # Local timeout testing utility
└── README.md
```

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/imAbishek/incident-processor.git
cd incident-processor
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
python -m pip install "fastapi[standard]" requests pytest httpx
```

**4. Run the CLI**

```bash
python main.py
```

**5. Run the FastAPI server**

```bash
fastapi dev api.py
```

Interactive API documentation: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/incidents` | Retrieve all incident records |
| GET | `/incidents?severity=high` | Filter incidents by severity |
| GET | `/incidents/summary` | Get total incidents and severity counts |
| POST | `/incidents` | Validate and return submitted incident data |

**Example — GET `/incidents/summary`**

```json
{
  "total_incidents": 5,
  "severity_count": {
    "high": 2,
    "medium": 1,
    "low": 1
  }
}
```

**POST `/incidents`** validates incoming JSON against the Pydantic `Incident` schema. Valid submissions return HTTP 200, while invalid request bodies return HTTP 422.

Note: POST currently validates and returns data without persisting it.

## Automated Tests

Run the complete test suite:

```bash
python -m pytest -q
```

Current test coverage:

| Test file | Tests | Coverage |
|---|---:|---|
| `test_processor.py` | 4 | Field validation, filtering, severity counting |
| `test_api.py` | 4 | GET endpoints, filtering, POST validation |
| `test_schemas.py` | 2 | Valid and invalid Pydantic models |
| **Total** | **10** | **All passing** |

## Current Limitations

- Incident records are loaded from a local JSON file; no database is integrated.
- POST requests validate data but do not save new incidents.
- The CLI checks required-field presence; Pydantic provides type validation for API requests.
- Tests use synthetic data, and some API tests depend on the existing JSON fixture.
- The standalone HTTP client is not integrated into the incident-processing pipeline.

## Project Progress

- **Week 1 — Python Essentials:** JSON processing, validation, reusable functions, HTTP error handling, CLI integration, and testing.
- **Week 2 — FastAPI Fundamentals:** REST endpoints, query parameters, Pydantic schemas, response contracts, refactoring, and automated API testing.

**Status:** Week 2 implementation complete