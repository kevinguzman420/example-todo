# app/public/models.py
"""
AUTOR: Gkvn

DATE CREATED: 21/02/2020
"""

# pip install mysql-connector-python
from app import db
import time

# class UserCat(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # It mean which this class has a relation with the class "User". This is a children:
#     user_id = db.Column(db.Integer, db.ForeignKey("task_user.id"), nullable=False)
#     cat_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

#     def save(self):
#         if not self.id:
#             db.session.add(self)
#         db.session.commit()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    date_create = db.Column(db.String(10), default=time.strftime("%x"), nullable=True)
    date_todo = db.Column(db.String(10), nullable=False)
    hour_todo = db.Column(db.String(6), nullable=False)
    done = db.Column(db.Boolean, default=False)

    # This is a foreignkey of Category:
    id_cate = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    # This is a foreignkey of Priority:
    id_prio = db.Column(db.Integer, db.ForeignKey("priority.id"), nullable=False)

    id_user = db.Column(db.Integer, db.ForeignKey("_user.id"), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_category = db.Column(db.String(64), nullable=False)
    # This table has a relation with the table "Task":
    task = db.relationship("Task", backref="category", lazy=False)

    @staticmethod
    def get_all():
        return Category.query.all()
        
    @staticmethod
    def get_by_name(name):
        return Category.query.filter_by(name_category=name).first()


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_priority = db.Column(db.String(64), nullable=False)

    task = db.relationship("Task", backref="priority", lazy=False)

    @staticmethod
    def get_all():
        return Priority.query.all()

    @staticmethod
    def get_by_name(name):
        return Priority.query.filter_by(name_priority=name).first()