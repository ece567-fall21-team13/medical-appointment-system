# Software Testing

## Approach / Details

The testing of our software will be done in three phases:
* Development Testing
* Release Testing
* User Testing

Development testing will proceed in this order: 
1. Unit testing
2. Component testing
3. System testing

## Unit tests
Each individual object class shall be tested separately by evaluating each method in the class by at least 3 separate values/conditions that lie in different equivalence partitions. Each class attribute should be retrieved and attempt to be set, to ensure proper visibility of class components are realized, and placing the class in all possible states.
In a feature iteration, these tests will be elaborated upon and could even be tested using an automation framework for unit testing.

### Test ideas
* Input validation
    * Illness category that doesn't match a known illness
    * Invalid patient id
    * Unavailable time slot requested for booking
    * Date in the past requested for booking
    * Unknown doctor requested for booking

## Component tests
Upon successful unit testing, component testing shall follow. This will include the interfaces that must interact between the various classes. Here we shall stress test the timing of one component interfacing with another, quickly repeating calls to another component, and testing parameters at the edges of parameter limits.

### Test ideas 
1. Overloading the interfaces of the APIs for getting a service, or booking a time slot, with quick, back-to-back requests, and observing how the components respond.
    * A testing tool, Locust, has been identified which allows for load testing by creating repeated calls to a service and tracking the system's response

## System tests
Upon successful completion of component testing, system testing shall proceed. Here we shall ensure that the system has integrated properly by evaluating the enumerated and developed use cases and ensure that the output matches what is expected.

### Test Ideas
1. Testing that a patient can receive an accurate schedule for any type of illness and then succesfully book it
2. Testing cases where the 14 day limit is potentially not abided by and ensuring the system properly conforms to that important constraint
2. Security testing (pen testing, encryption protocols for medical privacy, etc.)

## Use-case testing
Use cases tests will be added as more use cases are enumerated. Here we shall run through the system in the manner in which a user would as described in various use-cases.

## Release testing
Ideally, a separate team would perform their own testing of the system and check that the system meets its requirements. This could be done by having an outside group that is familiar with the problem statement analyze and use our system.

## User testing and user acceptance testing
1. Potential beta users
2. Users test across different platforms - does our service run equally well on mobile/web, Android/iOS?
3. Having potential patients use this software to book their appointments