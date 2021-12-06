from flask import Flask
from flask.templating import render_template

app = Flask('Calendar Demo')

events = [
    {
        'id' : '1',
        'title' : 'Appt. w/ Dr. Jha',
        'start' : '2021-12-06 16:00:00',
        'end' : '2021-12-06 17:00:00',
    },

    {
        'id' : '2',
        'title' : 'Appt. w/ Dr. Vogel',
        'start' : '2021-12-07 12:00:00',
        'end' : '2021-12-07 13:00:00',
    }
]

booked_events = [1, 2, 3];

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calendar.html')
def calendar():
    return render_template('calendar.html', 
    events = events)