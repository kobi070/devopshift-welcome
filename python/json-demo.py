from datetime import datetime
import json

# Python dictionary
data = {"name": "John", "age": 30, "city": "New York", "is_active": True, "countrey": None}
print(f"The data: {data} and the type: {type(data)}")

# Parse the data dictionary into a json file
json_data = json.dumps(data)
print(f"The data: {data} and the type: {type(data)}")

# Reparse the json file into a python dictionary
new_data = json.loads(json_data)
print(f"The new data: {new_data} and the type: {type(new_data)}")

