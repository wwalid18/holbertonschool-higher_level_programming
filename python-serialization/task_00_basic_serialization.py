#!/usr/bin/env python3
import json
"""serialization and deserialization of data"""


def serialize_and_save_to_file(data, filename):
    serialized_data = json.dumps(data)
    with open(filename, 'w') as file:
        file.write(serialized_data)


def load_and_deserialize(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())
