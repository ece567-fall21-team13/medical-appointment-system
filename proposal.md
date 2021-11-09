# Group 13 Project Proposal
**Project Problem #7:** 
You've been asked by the newly formed Rutgers Health to create a patient-doctor appointment system. Create a system that categorizes illness into N categories and doctor medical specialization into M categories (where N > M). Ideally, every patient will get a doctor with the right speciality but that could result in long waiting times.  You will need to make necessary assumptions of the number of patients, the number of doctors, acceptable waiting times (say based upon illness type) etc. but no patient must remain unseen for more than 14 days under any conditions.  

Methodology & Project Scope:

We propose to build an application that matches a patient to a physician with a specialty relevant to their illness. 
The application also involves a scheduling system which reserves an appointment time that is convenient both for the patient and the doctor.
The patient will be guided through an easy to follow, HIPAA compliant experience that will ensure their next appointment will be with the right physician at the earliest possible time.

Naturally, there are more possible medical conditions than there are specialties. 
As such, the pre-screening portion of the application plays a key part in directing a patient to the appropriate doctor. 
Each patient follows through a series of broad questions that allow the application to narrow down the doctor search space via hard-set rules involved in the decision-making procedure. 
Relevant corrections will be made given the severity of their issue, the availability of the doctor, and the flexibility of the patient to see a doctor which does not exactly match their needs, but is a more convenient choice for them.

The overarching issue faced by this project is a classic scheduling problem in which there are limited occupational resources (doctors) and a number of processes (patients). We will implement one of the following scheduling algorithms after analyzing which works best. 

    FCFS - First Come First Serve with Preemption

    Round Robin - Fixed Time Slice

    Priority Algo - based on the CRITICALITY etc.


The need for timely medical service for those in critical need of it must also be balanced with the availability of doctors (i.e. minimizing their downtime) and the convenience of all other patients.

There’s condition of starvation of patients must remain unseen for more than 14 days under any conditions.  This has been handled properly with prioritization. 



Apart from the integrity of the scheduling process, a major issue of this application is the security aspect. As such, careful detail will be paid to the security protocols and encryption standards in place for all sensitive data that the patient is sending through the portal. 
Goals:

This project’s success will be measured in various ways:

    Having a user interface for the patient to schedule themselves for appointments and have the ability to place their name and illness to be matched to a doctor.

    A user interface page that allows all events to be seen on a calendar.

    Having a database in which to store available doctors along with their speciality type, as well as the current list of appointments.

    Having an intelligent scheduling algorithm which first attempts to match a patient to the specific medical specialization, but leverages availability to ensure that each patient gets a match under 14 days.

Tools:

Flask calendar - a Flask Python API that allows for easy scheduling in a pseudo-Google calendar with HTML requests.

Flask SQLAlchemy - streamlines communication between Flask and data-storing Postgres

Flask - serving as the backend application.

React.js - serving as the front-end application which will make API requests to the Flask app

PostgreSQL - database for the application.

