from flask import Flask, request
from models import db
from getSchedule import getSchedule
from book import book

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'postgres',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

@app.route("/")
def main():
    return "App Succesfully Loaded"

@app.route("/schedule", methods=['GET'])
def get_schedule():
    return getSchedule(request.args)

@app.route("/book", methods=['POST'])
def post_booking():
    return book(request.args)

if __name__ == '__main__':
    app.run(debug=TRUE)