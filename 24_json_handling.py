# Exercise 24: JSON Parsing
# Task: Serialize a python dictionary to a JSON string and parse it back.

import json

def json_demo():
    data = {"name": "Bob", "skills": ["Python", "SQL"], "active": True}
    json_str = json.dumps(data)
    print("Serialized JSON string:", json_str)
    
    parsed = json.loads(json_str)
    print("Parsed dict:", parsed)

if __name__ == "__main__":
    json_demo()
