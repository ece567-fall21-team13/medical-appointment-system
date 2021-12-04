# Architectural Design
The Architectural Design phase in the first iteration entails an abstract discussion of the basic building blocks for our system. The following action items were assigned the highest priority as much of subsequent development hinges on their completion:


## Choose an architecture 
We'll be going with a more formal architecture pattern possibly service oriented architecture.
We'll be following SOLID principles alongside SOA.

## Language and Framework choice:
1. Application modality:
For universality and ease of access, we have decided to create a web application. A web application will ensure that we have the widest possible audience reach, and that there are likely to be fewer compatibility issues between various mobile OS releases.

2. In the preliminary stages of development, we have chosen to write our application in Python due to simplicity of syntax, universality of implementation, and prior group coding experience.

3. As the application is going to be web-based, we will be using the Flask web framework. The choice was made due to the vast array of existing Flask libraries that would ease our implementation and facilitate speedy delivery.

## Various components of the system

### UI Client 
The system can be accessible through mobile, web, tablets, etc. Based on the actor, the interfaces presented will be different, or a combination of many. So, individual interfaces will talk to the respective service for parts of the functionality. 
Primarily, there will be 2 portals of the interface for the three actors that is doctor and patients.

### IllnessCategorizerToSpecilizatonMapper Service
Gives specilizaiton based on illness category

### Schedule Availability Service - Major Service
schedule Slot of based on specilization 
Future scope may include fairness based on load 
Priority Element - Manually Controlled 
    * We'll mark the criticality of the illness category 
    * If the criticality we'll be open to secondary and tertiary specialization
    * If the criticality is medium we'll be open to secondary. 
After getting priority element - 
    * For Priority Default - 0 , we could book appointment for next 7 days 
    * Priority > 20 - we  could book for next 14 days

### Slot Booking Service - not to be handled/NOT considered in scope
Handle Concurrent slot booking problem here. 
There would be good chance that somebody is in the process of booking an appointment and somebody else also starts booking for sames slot.
It needs to be atomic and should update the availability as soon a slot is booked.


###  Choice of database -
We'll be choosing a RDBMS because of the nature for transactional system.
We need full ACID compliance.  

### Communication 
We will be following  RESTful web services pattern with JSON response
Choice of Database (eg. RDBMS, Document-based, KeyValue)


