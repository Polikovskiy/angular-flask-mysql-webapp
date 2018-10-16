from sqlalchemy import ForeignKey

from venv.app import db

class users(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    company = db.Column(db.Integer, ForeignKey('companys.id'))

    def __init__(self, name, email, company):
        self.name = name
        self.email = email
        self.company = company
