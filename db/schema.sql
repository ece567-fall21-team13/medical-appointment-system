CREATE
DATABASE mas;

CREATE TABLE doctor
(
    doctor_id   uuid PRIMARY KEY,
    doctor_name text,
    gender      text
);

CREATE TABLE patient
(
    patient_id    uuid PRIMARY KEY,
    patient_name  text,
    patient_email text
);

CREATE TABLE doctor_work_shift
(
    doctor_id   uuid REFERENCES doctor (doctor_id),
    shift_id    uuid PRIMARY KEY,
    shift_start time,
    shift_end   time,
    lunch_hour  time
);


CREATE TABLE appointment
(
    appointment_id uuid PRIMARY KEY,
    start_hour     time,
    end_hour       time,
    patient_id uuid REFERENCES patient (patient_id),
    doctor_id uuid REFERENCES doctor (doctor_id)
);


CREATE TABLE doctor_booked_schedule
(
    schedule_id    uuid,
    doctor_id uuid REFERENCES doctor (doctor_id),
    schedule_date  date,
    hour_number    time,
    schedule_event text, --Booked/Unavailable_DUE_TO_PRIORITY) - Keep in Diff (what really matters)
    appointment_id uuid REFERENCES appointment (appointment_id)
);

CREATE TABLE doctor_schedule_history
(
    schedule_id   text, -- NO FK
    doctor_id     uuid, -- NO FK
    patient_id    uuid,
    schedule_date date,
    hour_number   time
);

CREATE table doctor_specialization
(
    specialization_id   uuid PRIMARY KEY ,
    specialization_name text
);

CREATE table doctor_specialization_mapping
(
    doctor_id           uuid REFERENCES doctor (doctor_id),
    specialization_id   uuid REFERENCES doctor_specialization (Specialization_id),
    specilization_level text
);

CREATE TABLE illness_category
(
    category_id   uuid,
    category_name text,
    specialization_id uuid REFERENCES doctor_specialization (specialization_id)
);

CREATE TABLE patient_priority_schedule
(
    patient_id           uuid REFERENCES patient (patient_id),
    doctor_id            uuid REFERENCES doctor (doctor_id),
    requested_start_hour time,
    requested_end_hour   time,
    requested_date       time
);