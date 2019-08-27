import json

# some JSON:
from textwrap import indent

x = '{"name":"Mohamed", "age":22, "city":"cairo"}'

# parse x:
y = json.loads(x)

# result is python dict
print(y['age'])

# python to JSON
# a python object(Dict):
a = {
    "name": "Mohamed",
    "age": 23,
    "city": "gize"
}
# convert into JSON
b = json.dumps(a, indent=4, separators=(",", " = "),
               sort_keys=True)  # sort_keys to sort key values ,separetors defult (",",":") which is , comma and space for each object & colon with space to seprate key from value
# result is JSON string:
print(b)
