alter table doctor alter COLUMN doctor_id set default gen_random_uuid();

alter table patient alter COLUMN patient_id set default gen_random_uuid();


alter table appointment alter COLUMN appointment_id set default gen_random_uuid();

alter table appointment add COLUMN appointment_date date;

alter table doctor_booked_schedule alter COLUMN schedule_id set default gen_random_uuid();

alter table doctor_work_shift alter COLUMN shift_id set default gen_random_uuid();

alter table illness_category alter COLUMN category_id set default gen_random_uuid();

alter table illness_category  add primary key (category_id);

alter table doctor_specialization alter column specialization_id set default gen_random_uuid();

alter table doctor add column specialization_id uuid references doctor_specialization(specialization_id);