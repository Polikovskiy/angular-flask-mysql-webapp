from flask import Flask, render_template, json, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

class User(object):
    def __init__(self, Id, Name, Age):
        self.Id = Id
        self.Name = Name
        self.Age = Age


@app.route('/')
def index_page():
    return render_template("index.html")

@app.route("/users")
def get_users():
    '''user_json = {"Id":1, "Name":"Dmitriy", "Age":37}
    user_json['Id'] = 1
    user_json['Name'] = 'Dmitriy'
    user_json['Age'] = 37

    response = app.response_class(
        response=json.dumps(user_json),
        status=200,
        mimetype='application/json'
    )

    return response'''
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
    return response

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
