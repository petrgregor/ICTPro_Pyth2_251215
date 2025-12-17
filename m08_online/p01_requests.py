from pprint import pprint

import requests

result = requests.get("https://api.github.com/users/google")

print(f"result = {result}")

if result.status_code == 200:
    data = result.json()
    pprint(f"data = {data}")
    print(f"data['name'] = {data['name']}")
    print(f"data['email'] = {data['email']}")
else:
    print(f"ERROR: {result.status_code}")
