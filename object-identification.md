Object Identification  - 


1. Doctor - 
   1. doctor_id
   2. doctor_name
   3. gender

2. Doctor's Work Shift
   1. doctor_id
   2. shift_id
   3. shift_start hour
   4. shift_end hour
   5. lunch hour
   
3. Doctor's Booked Schedule  - Weekday x Hours matrix - Max 2/3 weeks -> 100*3*7*24 = 50400
   1. schedule_id
   2. doctor_id
   3. date: date >= 'Today'
   4. hour_number - Assumption minimum 1hr (0-24)
   5. schedule_event - Boolean (Blocked/Unavailable) - Keep in Diff (what really matters)
   6. appointment_id - 

|doctor_id| date| hour_number | schedule_event| Appointment_id
| ---|---|---|---|---|
| 101| '1 Nov 2021'| 0| Blocked| a101
| 101| '1 Nov 2021'| 2| Unavailable| NULL
| 101| '1 Nov 2021'| 11| Blocked| a102
| 101| '2 Nov 2021'| 0| Blocked| a103
| 101| '2 Nov 2021'| 1| Blocked|a103
| 101| '2 Nov 2021'| 2| Blocked|a103
```sql
9,11,14,15,16,17,18,19
(SELECT explodes(start_hour, end_hour) from doctor_work_shift --  9th hour - 15th hour 
9,10,11,12,13,14,15,16,17,18,19  --13th is lunch hour
negate JOIN
Doctor's Booked Schedule --> 10, 12
)
```

4. Appointment - Contiguous set of schedule hours 
   1. appointment_id
   2. start hour - 12:00
   3. end hour - 3:00
   4. patient_id
   5. doctor_id
   
| appointment_id| start_hour | end_hour | patient_id| doctor_id| 
| ----| ----|-----|-----|-----|
| a103| 0|3|p101|101|

3. Doctor's  Schedule History - (Probably not useful for core logic) - Scalable Design 
   2. schedule_id
   3. doctor_id
   4. date: date < 'Today' i.e. yesterday
   5. hour_number - Assumption minimum 1hr (0-24)
   6. is_available - Boolean (True/False)
4. P

[comment]: <> (3. Current Doctor Schedule Mapping )

[comment]: <> (   1. doctor_id)

[comment]: <> (   2. schedule_id)


3. Doctor's Available Schedule  - Weekday x Hours matrix - Max 2/3 weeks -> 100*3*7*24 = 50400
   1. schedule_id
   2. doctor_id
   3. start_time - timestamp
   4. end_time - timestamp
   5. appointment_id
   
4. Appointment
   1. appointment_id
   2. start hour - 12:00
   3. end hour - 3:00
   4. patient_id
   5. doctor_id




5. Specialization
   1. Specialization_id
   2. Specialization_name -> eg. Orthodontistry, SmileDesign, Dermatology, Gastroenterology, 

6. doctor_specilization_mapping
   1. doctor_id
   2. Specialization_id
   3. specilization_level - "Primary","Secondary","Tierarchy"

7. Illness Category
   1. category_id
   2. category_name (large) -> "Soar Throat ","Eye Strain","Low Eye Vision" , "Skin","Sprains", General Phyical Wellness
   3. specilization_id
