import json

def load_incidents(filename):
    try:
        with open(filename, "r") as file:
            incidents = json.load(file)
            return incidents
    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError:
        print("JSON Decode Error")
    return None