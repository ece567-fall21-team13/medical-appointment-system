Object Identification  - 


1. Doctor 
   1. doctor_id
   2. doctor_name
   3. gender

2. Doctor's Work Shift
   1. doctor_id
   2. shift_id
   3. shift_start hour
   4. shift_end hour
   5. lunch hour
   
> Note: https://www.postgresql.org/docs/9.3/rangetypes.html   
3. Doctor's Available Schedule  - Weekday x Hours matrix - Max 2/3 weeks -> 100*3*7*24 = 50400
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

4. Appointment
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
    
24hrs timeline data structure - support time window
   - Query - get all available slots at granualarity of timestam- 
   - eg. 12:21 - 12:08, 12:09 - 12:11
   - what we keep in state - 12:08 - 12:09

4. Appointment
   1. appointment_id
   2. start hour - 12:00
   3. end hour - 3:00
   4. patient_id
   5. doctor_id
