# System Modeling

System Modeling

This process entails development of abstract models of a system that helps present different perspectives of the system. In our case, we will present different models that represent the medical appointment system in a graphical notation based on UML. Some of the prespectives that are represented by various models explain: -

* External Perspective - It helps model the system environment. A context diagram placed below indicates different parts of the system that are being developed. The figure shows the medical appointment management system where the appoitment scheduling system is connected to doctor management system, patient management system and an admin/ system manager system. The context diagram help understand the boundaries of system and its environment.

  Place the diagram here....

  ```
  ![Requirements Engineering](assets/Context Diagram.drawio.png)
  ```

  The context model above shows the medical appointment system and other systems in its environment. The appoinment scheduling system is connected to the Doctor's portal that manages the availability of various doctors and helps the doctors to manage thier respective calender as well. The patients portal provides access to the patients to view the availability of doctors and book appointments. The appointment management system regulates the priority algorithm that optimizes the scheduler and makes sure that the patient's priority is upgraded so as to meet the 14 day appointment contraint.
* Interaction Perspective - This helps model the interactions between a system and its environment/ componenets of the system. This helps in identification of potential communication problems. Our case explains this perspective through the Use case and the sequence model for the appoitment scheduling system.

  Place the Use case diagram here.....

As seen in the diagram mapping system, doctor and the patient are the actors in the system. The 		doctor can view the patient records, appointment details and own schedule. The patient has the ability to search and book the appointment. The mapping system maps the patient's ailment to the required specialist and manages the appointment to serve the 14 day appointment constriant. The diagram helps understand different used cases that form the part of our appointment sceduling software system.

Place sequence model diagram here.......

The sequence diagram placed above models the interaction between actors and the objects in the appointment scheduling system. The sequence of interaction between the objects is as follows: -

The patient triggers the appointment booker object, which in turn maps it to the specialisation mapper. once the patient is mapped, the scheduler checks the earliest available slot and books it for the patient. In case the appointment is not available, the scheduler uses the optimization algorithm to raise the priority status of the patient's request to fulfill the 14 day appointment criteria.

* Structural perspective - The system organisation and the structure of the data processing is modeled here. Our case study explains this via class diagrams. Various objects that represented in the system are doctor, patient, calender based scheduler, admin login system. The class diagram is placed below.

```
Place the class diagram here.......
```

The class diagram helps develop an object oriented system model. In the class diagram above.......

* Behavioral perspective - Here we model the dynamic behavior of the system abd how it responds to events. A state diagram and a DFD is placed below to explain the behavioral perspective of medical appointment system. The scheduling data of the doctor and the patient generate the stimuli that triggers the system processing.

  Place the state diagram here.....

  As shown in the state diagram above,

Place the DFD diagram here.....

The DFDs help understand functional perspectives of the system and how the system processes the data. The DFD is simple and helps provide an intuitve understanding of the system. As seen in the Zero level DFD above, the central node of the system is the medical appointment system that has various functionalities built to manage different objects in the system.
