from flask import Flask, render_template, json, jsonify, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, session

#from models.user import users


app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.sqlite3'

db = SQLAlchemy(app)

class users(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    company = db.Column(db.Integer, ForeignKey('companys.id'))


    def __init__(self, name, email, company):
        self.name = name
        self.email = email
        self.company = company

class companys(db.Model):

    id = db.Column( db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    quota = db.Column(db.Integer)
    users = relationship("users", backref="companys")

    def __init__(self, name, quota):
        self.name = name
        self.quota = quota



@app.route('/')
def index_page():
    company = companys("coca-cola", 100000)
    user = users('kolia', 1, 'kolia@mail.ru')
    db.session.add(company)
    db.session.add(user)
    db.session.commit()

    return render_template("index.html")


@app.route("/users", methods = ['GET'])
def get_users():
    user_list = users.query.all()
    company_list = companys.query.all()
    user_json = []
    for user in user_list:
        user_dict = {}
        user_dict["Id"] = user.id
        user_dict["Name"] = user.name
        user_dict["Email"] = user.email
        #compan = companys.query.filter_by(id=user.company).first()
        #company = companys.query.get(user.company)
        company = session.query(companys).filter(companys.id == user.company)
        user_dict["Company"]  = company.quota
        user_json.append(user_dict)

    response = app.response_class(
        response=json.dumps(user_json),
        status=200,
        mimetype='application/json'
    )
    return response

'''@app.route("/users", methods = ['GET'])
def get_users():

    user = User(1, 'Dmitriy', 37)
    user2 = User(2, 'michail', 30)
    user_json = []
    user_list = []
    user_list.append(user)
    user_list.append(user2)

    for user in user_list:
        user_dict = {}
        user_dict["Id"] = user.Id
        user_dict["Name"] = user.Name
        user_dict["Age"] = user.Age
        user_json.append(user_dict)

    response = app.response_class(
        response=json.dumps(user_json),
        status=200,
        mimetype='application/json'
    )
    return response'''

@app.route("/users", methods = ['POST'])
def add_new_user():
    name = request.form['Name']
    email = request.form['Email']
    company = request.form['Company']
    user = users(name, email, company)
    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
