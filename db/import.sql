COPY doctor (doctor_id, doctor_name, gender,specialization_id)
    FROM '/home/workstation/workspace/PycharmProjects/medical-appointment-system/db/sample_data/doctor.csv'
    DELIMITER ','
    CSV HEADER;0


COPY patient (patient_id, patient_email, patient_name)
    FROM '/home/workstation/workspace/PycharmProjects/medical-appointment-system/db/sample_data/patient.csv'
    DELIMITER ','
    CSV HEADER;


COPY appointment (appointment_id,start_hour, end_hour, patient_id, doctor_id, appointment_date)
    FROM '/home/workstation/workspace/PycharmProjects/medical-appointment-system/db/sample_data/appointment.csv'
    DELIMITER ','
    CSV HEADER;

COPY doctor_booked_schedule (doctor_id,schedule_date,hour_number,schedule_event,appointment_id)
    FROM '/home/workstation/workspace/PycharmProjects/medical-appointment-system/db/sample_data/schedule.csv'
    DELIMITER ','
    CSV HEADER;

COPY doctor_work_shift (shift_id,doctor_id, shift_start, shift_end , lunch_hour)
    FROM '/home/workstation/workspace/PycharmProjects/medical-appointment-system/db/sample_data/doctor_work_shift.csv'
    DELIMITER ','
    CSV HEADER;

COPY doctor_specialization (specialization_id,specialization_name)
    FROM '/home/workstation/workspace/PycharmProjects/medical-appointment-system/db/sample_data/specialization.csv'
    DELIMITER ','
    CSV HEADER;

COPY illness_category (category_name,specialization_id)
    FROM '/home/workstation/workspace/PycharmProjects/medical-appointment-system/db/sample_data/illness_category.csv'
    DELIMITER ','
    CSV HEADER;



