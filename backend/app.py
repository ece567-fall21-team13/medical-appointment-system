from flask import Flask
from models import db
from mapper import IllnessToSpecializationMapper

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
    return 'Hello World !'

@app.route("/test")
def test():
    result = db.engine.execute("SELECT * FROM mas.doctor")
    dicts = []
    for r in result:
        row_as_dict = dict(r)
        dicts.append(row_as_dict)
    return "<h1>{}<h1><h2>{}</h2>".format(dicts[0]['doctor_name'], dicts[1]['doctor_name'])

@app.route("/mapper")
def mapperFnc():
    return IllnessToSpecializationMapper()
 
@app.route("/illness/<illnessName>")
def show_name(illnessName):
    return "<h1>Your have the: {}</h1>".format(illnessName)

# Services 
# Main appointment booker api which possible has a parameter name and a place to input illness
# IllnessToSpecializationMapper which takes that illness and maps it to a doctor specialization
# The Mapper then goes to the scheduler and says here is the specialization i want, show me the available doctors for that specialization schedule

if __name__ == '__main__':
    app.run(debug=TRUE)