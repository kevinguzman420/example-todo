from flask import render_template, url_for, redirect, request, g, flash
from .models import Category, Task, Priority
from app.auth.models import User
from flask_login import login_required, current_user
from app.models import Binnacle
from app import login_manager, db
import json
# from .forms import PostForm

from . import public_bp

@public_bp.route('/create/task/', methods=['GET', 'POST'])
@login_required
def create_task():
    context = {
        "categories": Category.get_all(),
        "priorities": Priority.get_all()
    }
    if request.method == 'POST':
        title = request.form['title-task']
        description = request.form['description-task']
        date_start = request.form['date-start-task']
        date_end = request.form['date-end-task']
        hour_task = request.form['hour-task']
        category = request.form['category-task']
        priority = request.form['priority-task']
        # Get the category and priority, to get their id's:
        category = Category.get_by_name(category)
        # print(category.id)
        priority = Priority.get_by_name(priority)
        # print("priority {0}".format(priority.id))
        try:
            # To add a new task:
            task = Task(title=title, description=description, date_create=date_start, date_todo=date_end, hour_todo=hour_task, done=False, \
                    id_cate=category.id, id_prio=priority.id, id_user=current_user.id)
            task.save()
            print("after the save method")
            flash('The task has been saved successfully', 'success')
            return redirect(url_for('public.index'))
        except:
            flash('Has ocurred a internal error, please retry again.', 'error')
            return redirect(url_for('public.create_task'))
    return render_template("public/create_task.html", **context)


@public_bp.route('/')
@login_required
def index():

    tasks = Task.query.join(User.usucat).join(Category).join(Priority).filter(User.id == current_user.id).all()
    context = {
        "tasks": tasks
    }
    for item in tasks:
        print(item.priority.name_priority)
    return render_template("public/index.html", **context)


@public_bp.route('/user/account/', methods=['GET', 'POST'])
@login_required
def account_user():
    return render_template("public/user_account.html")