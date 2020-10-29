import json
from decimal import Decimal


data = [{
    'id': 123,
    'entities': {
        'url': 'python.org',
        'hashtags': ['#python', '#pythonkor']}}]

print("dumps(data):", json.dumps(data, indent=2))

json_str = '["ham", 1.0, {"a":false, "b":null}]'
print("loads(json_str):", json.loads(json_str))

print("loads():", json.loads(json_str, parse_float=Decimal))

data = {
    "no": 5,
    "code": ("jas", 1, 19),
    "src": "be quick to listen, slow to speak, slow to anger"
}


filename = "test.json"
with open(filename, "w") as fp:
    fp.write(json.dumps(data))


with open(filename, "r") as fp:
    r = json.load(fp)
    print("no:", r["no"])
    print("code:", r["code"])
    print("src:", r["src"])
