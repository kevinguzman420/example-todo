"""
AUTOR: Gkvn

DATE CREATED: 21/02/2020

"""

from app import db

class Binnacle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    date_create = db.Column(db.DateTime, nullable=False)
    date_todo = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, default=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()