from flask import Flask, render_template, json, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, update
from sqlalchemy.orm import relationship, session
from resourses.res import *
#from models.user import users


app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.sqlite3'

db = SQLAlchemy(app)

TRANSFER_LOG_LIST = []




class companys(db.Model):

    id = db.Column( db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    quota = db.Column(db.Integer)
    users = relationship("users", backref="companys")

    def __init__(self, name, quota):
        self.name = name
        self.quota = quota


class users(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    company = db.Column(db.Integer, ForeignKey('companys.id'))

    def __init__(self, name, email, company):
        self.name = name
        self.email = email
        self.company = company


class transfer_log(object):

    def __init__(self, date, name, resourses, company_id):
        self.date = date
        self.name = name
        self.resourses = resourses
        self.transferred = transfer_data_volume()
        self.company_id = company_id

    def __str__(self):
        return  "date: " + self.date + " name: " + self.name + " transferred: " + str(self.transferred)

    def __repr__(self):
        return  "date: " + self.date + " name: " + self.name + " transferred: " + str(self.transferred)


class company_ubsusers(object):

    def __init__(self, name, quota, used):
        self.name = name
        self.quota = quota
        self.used = used

    def __str__(self):
        return   " name: " + self.name + " used: " + str(self.used) + " quota: " + str(self.quota)

    def __repr__(self):
        return " name: " + self.name + " used: " + str(self.used) + " quota: " + str(self.quota)


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route("/users", methods = ['GET'])
def get_users():

    user_list = users.query.all()
    user_json = []

    for user in user_list:

        user_dict = {}
        user_dict["Id"] = user.id
        user_dict["Name"] = user.name
        user_dict["Email"] = user.email
        user_dict["Company"]  = companys.query.filter_by(id=user.company).first().name
        user_json.append(user_dict)

    return jsonify(user_json)


@app.route("/users", methods = ['POST'])
def add_new_user():
    user_reuqest = request.get_json()

    if user_reuqest:

        new_user = users(user_reuqest['Name'], user_reuqest['Email'], int(user_reuqest['Company']))
        db.session.add(new_user)
        db.session.commit()

        return jsonify("ok")

    else:

        return jsonify("failure")


@app.route("/users", methods = ["DELETE"])
def delete_user():

    if request.args.get("id"):

        deleted_user = users.query.filter_by(id=request.args.get("id")).first()
        db.session.delete(deleted_user)
        db.session.commit()

    return jsonify("ok")


@app.route("/users", methods = ["PUT"])
def update_user():

    user_request = request.get_json()

    if user_request:

        user = users.query.filter_by(id=user_request['Id']).first()
        user.email = user_request['Email']
        user.name = user_request['Name']
        user.company = user_request['Company']
        db.session.commit()

        return jsonify("ok")

    else:

        return jsonify("failure")


@app.route("/company")
def company():
    company_list = companys.query.all()
    company_json = []
    for company in company_list:
        company_dict = {}
        company_dict["Id"] = company.id
        company_dict["Name"] = company.name
        company_dict["Quota"] = company.quota
        company_json.append(company_dict)

    return jsonify(company_json)


@app.route("/company", methods = ['POST'])
def add_new_company():
    company = request.get_json()

    if company:

        new_company = companys(company['Name'], company['Quota'])
        db.session.add(new_company)
        db.session.commit()

    return jsonify("ok")


@app.route("/company", methods = ["PUT"])
def update_company():

    company_request = request.get_json()

    if company_request:

        company = companys.query.filter_by(id=company_request['Id']).first()
        company.name = company_request['Name']
        company.quota = company_request['Quota']
        db.session.commit()

        return jsonify("ok")

    else:

        return jsonify("failure")



@app.route("/generate_data")
def generate_data():

    user_list = users.query.all()
    company_list = companys.query.all()
    transfer_log_list = [[],[],[],[],[],[]]

    for user in user_list:
        user_date_transfer_list  = transfer_date_list(list_6_random_numbers())

        for month in user_date_transfer_list:
            transfer_log_list_month = []

            for date in month:
                user_transfer_log = transfer_log(date, user.name, "http/xxx.xxx.xxx", user.company)
                transfer_log_list_month.append(user_transfer_log)
            transfer_log_list[user_date_transfer_list.index(month)]  += transfer_log_list_month




    global TRANSFER_LOG_LIST
    TRANSFER_LOG_LIST = transfer_log_list



    return jsonify('ok')


@app.route("/show", methods = ['POST'])
def show():

    ubsusers_list = []
    company_ubsusers_json = []
    request_month = request.get_json()
    company_list = companys.query.all()

    for company in company_list:
        company_traffic = 0

        for month in TRANSFER_LOG_LIST:

            if TRANSFER_LOG_LIST.index(month) >= request_month:
                pass

            for log in month:

                if log.company_id == company.id:
                    company_traffic += log.transferred

        company_quota = company.quota * request_month

        if company_traffic > company_quota:

            company_ubsuser = company_ubsusers(company.name, company_quota, company_traffic)
            ubsusers_list.append(company_ubsuser)

    for company in ubsusers_list:
        ubsuser_dict = {}
        ubsuser_dict["Name"] = company.name
        ubsuser_dict["Quota"] = company.quota
        ubsuser_dict["Used"] = company.used
        company_ubsusers_json.append(ubsuser_dict)

    #return jsonify([{"ubsusers" : company_ubsusers_json}, {"transfer_log" : transfer_log_json}])
    return  jsonify(company_ubsusers_json)


if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
