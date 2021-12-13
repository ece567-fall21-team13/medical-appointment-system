WITH appointment_ins AS (
    INSERT INTO appointment
        (start_hour, end_hour, patient_id, doctor_id, appointment_date)
--         Take these arguments from application
        VALUES ('13:00:00', '16:00:00', '3f4c41a0-1e95-40f3-85d2-df0d49f5f915', 'a556ad27-5b14-40b5-837f-f857059f727a',
                '2021-12-14')
        RETURNING appointment_id)
INSERT
INTO doctor_booked_schedule
    (doctor_id, schedule_date, hour_number, schedule_event, appointment_id)
--     Take these arguments from application
SELECT 'a556ad27-5b14-40b5-837f-f857059f727a',
       '2021-12-14',
       (generate_series(extract(hour from '13:00:00'::time)::int, (extract(hour from '16:00:00'::time)::int -1) ) || ':00:00')::time
        ,
       'Booked',
       appointment_id
FROM appointment_ins
returning appointment_id;