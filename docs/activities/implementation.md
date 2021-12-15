# Implementation (from Design and Implementation)
## Methods of Implementation
Implementation is concerned with creating an executable version of the software.

For this system, the Flask framework written in Python will be used to create the "backend" services of the system. REST APIs and endpoints will be created for the critical functionality of the system such as finding the available schedules and booking a schedule slot. These will be created in accordance with the design created in [specification.md](./specification.md).

Having a data model and a permanent method to store data was also identified as necessary. For this, a PostgreSQL relational database will be created with the data objects identified in the specification. This will be needed in order to permanently store what slots are available and what slots have been booked, and keeping track of other related data.

## RESTful API Endpoints
### /schedule
The `/schedule` endpoint is a `GET` request which takes one argument: `illnessCategory`. 
- Sample request:
```
    localhost:5000/schedule?illnessCategory=braces
```
- Partial sample response:
```json
[
  {
    "availability": "Booked", 
    "category_name": "braces", 
    "doctor_id": "a556ad27-5b14-40b5-837f-f857059f727a", 
    "doctor_name": "Lilly Brady", 
    "shift_date": "Mon, 13 Dec 2021 00:00:00 GMT", 
    "shift_hour": 9, 
    "specialization_name": "Orthodontics"
  }, 
  {
    "availability": "Booked", 
    "category_name": "braces", 
    "doctor_id": "a556ad27-5b14-40b5-837f-f857059f727a", 
    "doctor_name": "Lilly Brady", 
    "shift_date": "Mon, 13 Dec 2021 00:00:00 GMT", 
    "shift_hour": 10, 
    "specialization_name": "Orthodontics"
  },
  ...
]
```

### /book
The `/book` endpoint is a `POST` request which takes five arguments: `appointment_date`, `doctor_id`, `patient_id`, `start_hour`, and `end_hour`.
- Sample request:
```
    localhost:5000/book?appointment_date=2021-12-13&doctor_id=a556ad27-5b14-40b5-837f-f857059f727a&patient_id=fc6080cd-1fe5-4b66-ab25-3b634af4bf7e&start_hour=14&end_hour=15
```
- Sample response:
```json
{ 
    "appointment_id": "ea8727b3-93ab-4998-b7e5-e16846cf5184"
}
```

Next, is a discussion of particularly important software implementation issues that are addressed:

### Configuration management
Git and GitHub have been identified and used extensively to assist with configuration management. Detailed commits and branches representing iterations have been utilized to help the team with version management, system integration, and problem tracking.

### Host-target development
Our team has had various different development platforms, varying among OS and tools used. However, because we are using a web framework like Flask and a common SQL database like PostgreSQL, the target platform is not of too great concern. The Flask app is web-based and so can be deployed onto a web server, and PostgreSQL has plentiful documentation for usage. 

Our availability requirements have also been noted as high because of the importance of a medical appointment system, and so components/endpoints might need to be deployed on more than one platform to aid in redundancy and fault tolerance.