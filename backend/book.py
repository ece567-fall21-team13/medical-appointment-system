from marshmallow import Schema, fields, ValidationError
from flask import jsonify
from sqlalchemy.sql import text
from models import db

class BookInputSchema(Schema):
    start_hour = fields.Integer(required=True) # Looks like '13:00:00'
    end_hour = fields.Integer(required=True) # Looks like '16:00:00'
    patient_id = fields.String(required=True) # Looks like 'UUID STRING'
    doctor_id = fields.String(required=True) # Looks like 'UUID STRING'
    appointment_date = fields.String(required=True) # Looks like '2021-12-14'

def book(args):
    try:
        input = BookInputSchema().load(args)
    except ValidationError as err:
        print(err.messages)
        return "Invalid input", 400
    
    query = """WITH appointment_ins AS (
                INSERT INTO mas.appointment
                    (start_hour, end_hour, patient_id, doctor_id, appointment_date)
            --         Take these arguments from application
                    VALUES ({startHr}, {endHr}, {patientID}, {doctorID},
                            {apptDate})
                    RETURNING appointment_id)
            INSERT
            INTO mas.doctor_booked_schedule
                (doctor_id, schedule_date, hour_number, schedule_event, appointment_id)
            --     Take these arguments from application
            SELECT {doctorID},
                {apptDate},
                (generate_series(extract(hour from {startHr}::time)::int, (extract(hour from {endHr}::time)::int -1) ) || ':00:00')::time
                    ,
                'Booked',
                appointment_id
            FROM appointment_ins
            returning appointment_id;""".format(startHr = "\'" + str(input['start_hour']) + ":00:00\'", endHr = "\'" + str(input['end_hour']) + ":00:00\'",
                                                patientID = "\'" + input['patient_id'] + "\'", doctorID = "\'" + input['doctor_id'] + "\'",
                                                apptDate = "\'" + input['appointment_date'] + "\'")

    result = db.engine.execute(text(query).execution_options(autocommit=True))
    appointment = {'appointment_id': ""}
    for r in result:
        row_as_dict = dict(r)
        appointment['appointment_id'] = row_as_dict['appointment_id']

    return jsonify(appointment)