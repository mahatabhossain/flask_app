from flask import request, jsonify
from jsonschema import validate, ValidationError

# Example JSON Schema
json_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name", "age"]
}

def validate_json():
    try:
        print('JSON validator API called')
        json_data = request.json
        print(json_data)
        validate(instance=json_data, schema=json_schema)
        return jsonify({'message': 'JSON data is valid.'}), 200
    except ValidationError as e:
        return jsonify({'error': e.message}), 400