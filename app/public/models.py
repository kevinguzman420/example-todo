# app/public/models.py
"""
AUTOR: Gkvn

DATE CREATED: 21/02/2020
"""

# pip install mysql-connector-python
from app import db
import time

class UserCat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # It mean which this class has a relation with the class "User". This is a children:
    user_id = db.Column(db.Integer, db.ForeignKey("task_user.id"), nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_category = db.Column(db.String(64), nullable=False)
    # This table has a relationship with the table "UserCat":
    catusu = db.relationship("UserCat", backref="category", lazy=False)
    # This table has a relation with the table "Task":
    task = db.relationship("Task", backref="category", lazy=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    date_create = db.Column(db.DateTime, default=time.strftime("%x"))
    date_todo = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, default=False)

    # This is a foreignkey of Category:
    id_cate = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    # This is a foreignkey of Priority:
    id_prio = db.Column(db.Integer, db.ForeignKey("priority.id"), nullable=False)

class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_priority = db.Column(db.String(64), nullable=False)
    task = db.relationship("Task", backref="priority", lazy=False)
