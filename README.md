# Incident Data Processor

## Overview

Incident Data Processor is a Python command-line application that loads incident records from a JSON file, validates required fields, and filters incidents based on severity.

The project was built as part of a practical Python learning sprint to understand JSON handling, functions, modules, exception handling, HTTP requests, and automated testing.

## Project Structure

```text
incident-processor/
├── main.py
├── file_loader.py
├── incident_processor.py
├── api_client.py
├── incidents.json
├── test_processor.py
├── slow_server.py
└── README.md
```

### Module Responsibilities

- **main.py** — Entry point of the application. Coordinates loading, validation, filtering, and displaying results.
- **file_loader.py** — Loads JSON files and handles file-not-found and invalid JSON errors.
- **incident_processor.py** — Contains reusable functions for filtering incidents, checking missing fields, and validating multiple records.
- **api_client.py** — Demonstrates HTTP GET requests, JSON response parsing, timeouts, and connection error handling. This module is currently separate from the main incident-processing workflow.
- **incidents.json** — Contains sample incident records used by the application.
- **test_processor.py** — Contains assertion-based tests for validation and filtering.
- **slow_server.py** — A temporary local HTTP server used to test request timeout handling.

## Features

### 1. JSON File Loading
- Loads incident records from `incidents.json`.
- Handles missing files using `FileNotFoundError`.
- Handles malformed JSON using `JSONDecodeError`.

### 2. Incident Validation
- Checks whether incidents contain four required fields:
  - `id`
  - `title`
  - `severity`
  - `status`
- Reports missing fields along with their incident IDs.
- Supports validating multiple incident records.

### 3. Severity Filtering
- Filters incident records based on severity.
- Displays high-severity incidents with their IDs and titles.
- Excludes records missing required fields before filtering.
- Continues processing valid records even when other incidents are invalid.

### 4. HTTP Integration
- Fetches JSON data from a public API using Python's `requests` library.
- Checks HTTP response status using `raise_for_status()`.
- Handles HTTP errors, request timeouts, and connection failures.
- Returns parsed JSON data when the request succeeds.

### 5. Automated Tests
- Uses Python assertions to verify expected results.
- Tests individual incident validation.
- Tests batch validation.
- Tests severity filtering and record exclusion.

## Requirements

- Python 3.11 or later
- `requests` library for the optional HTTP integration

## How to Run

### 1. Navigate to the project directory

```bash
cd incident-processor
```

### 2. Create and activate a virtual environment (if needed)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install the HTTP client dependency

```bash
python -m pip install requests
```

### 4. Run the Incident Processor

```bash
python main.py
```

The program loads `incidents.json`, checks the records for missing fields, and displays the high-severity incidents found among valid records.

## Example Output

```text
=== Incident Data Processor ===
3
Incident: 103 | Missing Fields: ['status']
=== High Severity Data Processor ===
ID: 101 | System unavailable
```

This output illustrates a dataset containing three records, one of which is missing its `status` field.

## Testing

Run the existing tests using:

```bash
python test_processor.py
```

Expected output:

```text
Missing-field test passed
Batch-validation test passed
Severity filtering test passed
```

The tests use Python's built-in `assert` statement.

If an assertion fails, Python raises an `AssertionError`, helping identify unexpected behavior.

### Test Coverage

| Test | Purpose |
|---|---|
| `test_missing_fields()` | Verifies that missing required fields are detected |
| `test_batch_validation()` | Verifies error count, incident ID, and missing fields for multiple records |
| `test_severity_filtering()` | Verifies that only incidents with the requested severity are returned |

## Error Handling

### Missing JSON File

If the requested file does not exist, the loader catches `FileNotFoundError` and returns `None`.

The main application detects this failure and displays:

```text
File not found
Cannot process incidents
```

### Invalid JSON

If the JSON file contains invalid syntax, the loader catches `JSONDecodeError` and returns `None`.

The application prevents further incident processing.

### Missing Incident Fields

If an incident is missing required fields, the program reports the incident ID and missing fields.

For example:

```text
Incident: 103 | Missing Fields: ['status']
```

The invalid record is excluded from severity filtering, while other valid incidents continue to be processed.

### HTTP Request Errors

The HTTP client handles:
- `HTTPError` — An HTTP error response detected by `raise_for_status()`.
- `Timeout` — A network operation exceeds its configured timeout.
- `ConnectionError` — A connection cannot be established or is disrupted.

The client returns `None` when one of these handled request failures occurs.

## Current Limitations

- Input validation checks the presence of required fields, not their data types or allowed values.
- The application expects a JSON list containing incident dictionaries.
- Incident severity filtering is currently fixed to `high` in the CLI.
- HTTP integration is implemented separately and is not connected to the incident-processing pipeline.
- The project uses basic assertion-based tests rather than a dedicated testing framework.

## Future Improvements

The next development stage is to convert the existing Incident Data Processor into a REST API using FastAPI.

Planned improvements include:

- API endpoints for accessing and filtering incidents.
- Request and response validation using Pydantic.
- Automated endpoint testing using pytest.
- Improved error responses and input validation.

## Project Status

**Week 1 — Python Essentials Sprint: Core implementation and tests completed.**

The project demonstrates practical Python fundamentals through a small, modular, working application.