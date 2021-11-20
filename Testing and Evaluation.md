# Testing and Evaluation

Be definition, a medical appointment system is a safety critical system that is required to be available 24/7 with minimum service interruptions, as much of the data transferred is both sensitive and critical.

As such, there are multiple vectors from whih the Testing and Evaluation issue is approached. Outlined below are some testing approached that can be implemented at any time of delivery of the product. That is, any time in the development process, after the MVP of the first sprint is shipped, the following tests can be used to diagnose the operation condition of the system, and gather insights into user satisfaction with the product. The tests are designed to be both qualitative and quantitave. That means that they will be able to capture som eobjective performance of the system, as well as outline user sentiment relevant to the system performance. 

- Gathering statistics on the latency of the system.
  - The system is likely to be used by a number of people at the same time, as it will be implemented in a large clinic. The system must be reliable, as it is of high importance, and must accomodate a high throughput. Therefore, a performance reliabilty standard must be put in place to accomodate the functional requirements of the system. A sensible standard to set is to ensure that the system is capable of handling up to 20,000 requests per second coming from different IP addresses. Additionally, it is appropariate to assume that the system be non-operation for nolonger than 15 minutes per month, as required by the maintanance team.
- Correct referral metrics.
  - The first componenet of the system is guaranteeing that the patient (user) is matched to the right specialist according to their specifications. In many cases, the patient will know exactly which specialist they would like to see *a priori*, however some might need more guidance with regards to their physican selection. As such, the decision tree off which the physician seleciton is based of must be fine tuned to refer the patient to the correct doctor with minimum necessary steps. To evaluate the performance of the subspecialty sugesstion system, the following two metrics and standards can be employed:
    - For patients that know which physician they want to see, ensure that the system assigned them to a correct physician. The aim is to have a >80% correct referral rate, as booking a physician can be a time-consuming process.
    - For patients who do not know which physician they would like to see, have an after-consultation survey to ensure that they have been assigned to a correct subspecialty physician. That will ensure that the system is working well for users who don't know their goal too well. The aim is to have a >70% sucess rate with this category of users.
- Appropriate time selection.
  - Timing your visit is important for both the consumers and 


