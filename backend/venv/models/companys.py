from sqlalchemy.orm import relationship

from venv.app import db


class companys(db.Model):

    id = db.Column( db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    quota = db.Column(db.Integer)
    users = relationship("users", backref="companys")

    def __init__(self, name, quota):
        self.name = name
        self.quota = quota