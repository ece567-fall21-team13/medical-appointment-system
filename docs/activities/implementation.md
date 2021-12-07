# Implementation (from Design and Implementation)
## Methods of Implementation
Implementation is concerned with creating an executable version of the software.

For this system, the Flask framework written in Python will be used to create the "backend" services of the system. REST APIs and endpoints will be created for the critical functionality of the system such as finding the available schedules and booking a schedule slot. These will be created in accordance with the design created in [specification.md](./specification.md).

Having a data model and a permanent method to store data was also identified as necessary. For this, a PostgreSQL relational database will be created with the data objects identified in the specification. This will be needed in order to permanently store what slots are available and what slots have been booked, and keeping track of other related data.

Here is a discussion of particularly important software implementation issues that are addressed:
### Reuse

### Configuration management

### Host-target development