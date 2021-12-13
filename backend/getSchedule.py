from marshmallow import Schema, fields, ValidationError
from flask import jsonify
from models import db

class GetScheduleInputSchema(Schema):
    illnessCategory = fields.String(required=True)

def getSchedule(args):
    try:
        input = GetScheduleInputSchema().load(args)
    except ValidationError as err:
        print(err.messages)
        return "Invalid input", 400

    query = """SELECT shift_date ,shift_hour ,availability ,   doctor_name ,category_name, specialization_name from
            (SELECT s.*, d.doctor_name, d.specialization_id
                from (SELECT dws.doctor_id,
                            shift_date,
                            shift_hour,
                            CASE when schedule_event = 'Booked' then 'Booked' else 'Available' end as availability
                        from (
                                select doctor_id,
                                        shift_hour,
                                        generate_series(CURRENT_DATE, CURRENT_DATE + '2 days'::interval,
                                                        '1 day'::interval)::date as shift_date
                                from (select doctor_id,
                                            shift_id,
                                            generate_series(extract(hour from shift_start)::int,
                                                            extract(hour from shift_end)::int) as shift_hour
                                    from mas.doctor_work_shift
                                    ) dsa

                                        LEFT JOIN
                                    (SELECT shift_id, extract(hour from lunch_hour)::int as lunch_hour
                                    from mas.doctor_work_shift
                                    ) sh
                                    on dsa.shift_id = sh.shift_id and dsa.shift_hour != sh.lunch_hour
                                where sh.shift_id is not null

                                order by 3, 2
                            ) dws
                                LEFT JOIN
                            (
                                select doctor_id, schedule_event, schedule_date, extract(hour from hour_number) as hour_number
                                from mas.doctor_booked_schedule
                            ) dbs
                            ON dws.doctor_id = dbs.doctor_id and dws.shift_hour = dbs.hour_number and
                                dws.shift_date = dbs.schedule_date) s
                        JOIN (SELECT doctor_name, doctor_id, specialization_id from mas.doctor) d
                                on s.doctor_id = d.doctor_id) ds
                    JOIN
                (select category_name, specialization_name, i.specialization_id
                from mas.illness_category i
                        join mas.doctor_specialization s on i.specialization_id = s.specialization_id) ism
                on ism.specialization_id = ds.specialization_id
        WHERE category_name = {0};""".format("\'" + input['illnessCategory'] + "\'")
    
    result = db.engine.execute(query)
    dictOfMatchingSlots = []
    for r in result:
        row_as_dict = dict(r)
        dictOfMatchingSlots.append(row_as_dict)

    return jsonify(dictOfMatchingSlots)