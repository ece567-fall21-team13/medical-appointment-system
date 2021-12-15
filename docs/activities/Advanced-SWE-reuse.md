# Advances SWE - Reuse

One of the primary objectives in designing this application was to focus on the reuse of existing, off-the-shelf tools for both the ease of building this calendar application, as well as simplifying the modifications to this application in future calendar work for different scheduling tasks.

The entire front-end component of the system was designed using FullCalendar, a partially open-source development tool for all calendar styles. It supports all basic scheduling and booking functionalities. The open source version contains all necessary components for our application, as we primarily rely on blocking off available times and displaying those times to the user. More advanced fetures, available in the paying version of FullCalendar, are largely useless for our scheduling applications, as they involve more complex GSuite-type tasks like drag and drop features, as well as cross-device synchroniation and others.

Additionally, our application is a perfect candidate for reuse in other scheduling tasks for medical systems which do not have our exact specifications. Any additional parameters that must be saved within the appointment object are strictly defined in the FullCalendar API and can be modified in only 2 places in the entire application that will render them available everywhere. 

For instance, if the system was to be repurposed for an appointment scheduler with a parameter that accounted for appointment room, that could be easily placed in the front end via FullCalendar. 

