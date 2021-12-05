from marshmallow import Schema, fields, ValidationError
from flask import jsonify

class BookInputSchema(Schema):
    schedule_date = fields.Date(required=True)
    doctor_id = fields.Integer(required=True)
    patient_id = fields.Integer(required=True)
    start_hour = fields.Integer(required=True)
    end_hour = fields.Integer(required=True)

def book(args):
    try:
        input = BookInputSchema().load(args)
    except ValidationError as err:
        print(err.messages)
    try:
        return jsonify(input)
    except NameError:
        return "Invalid input", 400

## To return: associated appointment_id, start_hour, end_hour
# Todo: Create class for return value
# Todo: logic for querying the database and returning