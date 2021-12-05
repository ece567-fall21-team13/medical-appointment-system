from marshmallow import Schema, fields, ValidationError
from flask import jsonify

class GetScheduleInputSchema(Schema):
    illnessCategory = fields.String(required=True)
    patient_id = fields.Integer(required=True)

def getSchedule(args):
    try:
        input = GetScheduleInputSchema().load(args)
    except ValidationError as err:
        print(err.messages)
    try:
        return jsonify(input)
    except NameError:
        return "Invalid input", 400

## To return: list of available schedules
# Todo: Create class for a schedule slot
# Todo: logic for querying the database and returning