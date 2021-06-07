#!/usr/bin/env python3

import json
from jsonschema import validate

with open("schemas/network.json") as schemafile:
    schema = json.loads(schemafile.read())
with open("examples/network1.json") as inputfile:
    input = json.loads(inputfile.read())

print(schema)
validate(instance=input, schema=schema)


