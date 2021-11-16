# Requirements Engineering

## Requirements Elicitation and Analysis

### Requirements Discovery
The requirements elicitation process starts with requirements discovery. For this project, we decided to observe the current Rutgers Health appointment system as a form of interviewing to discover and understand requirements.

From this, we discovered that the current system:
1. Requests the patient choose a purpose of the visit
2. Confirms the reason for the visit
3. And then allows the patient to choose an available data and time

### Requirements Classification and Organization
With the knowledge of the current system, two types of requirements come to mind:
- Matching the patient's illness to doctors
- Display availability for matching doctors

### Requirements Documentation
The resulting preliminary requirements from this analysis combined with the problem statement amount to:
- The system shall allow the patient to define the illness they have
- The system shall match a patient to a doctor based on their illness
- The system shall display the available times of qualified doctors for a patient to select 
- If no doctors exactly match, the system shall display available times of the "next best" doctors for the patient to select to achieve the less than 14 day seeing time constraint

## Requirements Specification

### Functional Requirements
ID | Description
--- | ---
FREQ-1 | The system shall allow a patient to make an appointment for their illness.
FREQ-2 | The system shall assign the patient's illness to a specific illness category.
FREQ-3 | The system shall display the availability of the doctors whose medical specialization matches the illness category.
FREQ-4 | In the case no doctor with matching medical specializations is available within 14 days, the system shall display the availability of doctors who most closely match the needed specialization.
FREQ-6 | The system shall allow multiple patients to schedule an appointment simultaneously.
FREQ-7 | The system shall minimize waiting times for more severe illnesses.

### Non-functional Requirements
ID | Description
--- | ---
NFREQ-1 | The system shall ensure every patient is seen within 14 days.
NFREQ-2 | The system's availability should be greater than .999.
NFREQ-3 | The storage of the patient's health information must conform to HIPAA standards.


## Requirements Validation