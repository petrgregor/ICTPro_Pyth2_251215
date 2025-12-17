import json

from m06_serialization.p01_pickle import DataContainer

data = {
    "product_id": 25,
    "product_name": "Notebook",
    "product_price": 14599,
    "tags": ["computer", "notebook", "office"]
}


json_str = json.dumps(data)  # -> str
print(f"json_str: {json_str}")

reloaded_data = json.loads(json_str)
print(f"reloaded_data = {reloaded_data}")


# Serialization
try:
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
except Exception as e:
    print(f"ERROR: {e}")

# Deserialization
try:
    with open("data.json", "r") as f:
        reloaded_data2 = json.load(f)
        print(f"reloaded_data2 = {reloaded_data2}")
except Exception as e:
    print(f"ERROR: {e}")

data_container = DataContainer(99)
print(f"data_container.to_json(): {data_container.to_json()}")
try:
    with open("data_container.json", "w") as f:
        json.dump(data_container.to_json(), f, indent=4)
except Exception as e:
    print(f"ERROR: {e}")

try:
    with open("data_container.json", "r") as f:
        reloaded_json = json.load(f)
        print(f"reloaded_json = {reloaded_json}")
        reloaded_data_container = DataContainer(reloaded_json['value'])
        print(f"reloaded_data_container = {reloaded_data_container}")
except Exception as e:
    print(f"ERROR: {e}")