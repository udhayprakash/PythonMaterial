import copy
from pprint import pp

payload = {
    "DOB": "-",
    "age": 25,
    "education": {"college": "Yale", "highschool": "N/A"},
    "hobbies": ["running", "coding", "-"],
    "name": {"first": "Robert", "last": "Smith", "middle": ""},
}


pp(payload)

payload1 = copy.deepcopy(payload)

for key, value in payload.items():
    if isinstance(value, (str, int, float)):
        if value in ("N/A", "-", ""):
            del payload1[key]
    elif isinstance(value, list):
        payload1[key] = [s_val for s_val in value if not (value in ("N/A", "-", ""))]
    elif isinstance(value, dict):
        for skey, sval in value.items():
            if sval in ("N/A", "-", ""):
                del payload1[key][skey]

print()
pp(payload1)
