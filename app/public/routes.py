from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user
from .models import Category, Task, Priority
from app.auth.models import User
from app.models import Binnacle
from flask_login import login_required, current_user
from app import login_manager, db
import json
# from .forms import PostForm

# from auth import g
from . import public_bp

# @public_bp.before_request
# def before_request():
#     g.user = current_user
#     # print(current_user.username)

@public_bp.route('/create/task/', methods=['GET', 'POST'])
@login_required
def create_task():
    context = {
        "categories": Category.get_all(),
        "priorities": Priority.get_all(),
        "flag": False
    }
    message = None
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
            message = 'The task has been saved successfully'
            flash(message, 'success')
            return redirect(url_for('public.index'))
        except:
            flash('Has ocurred a internal error, please retry again.', 'error')
            return redirect(url_for('public.create_task'))
    return render_template("public/create_task.html", **context)


@public_bp.route('/')
@login_required
def index():
    tasks = Task.query.join(User.usucat).join(Category).join(Priority).filter(User.id == current_user.id).order_by(Task.done).all()
    context = {
        "tasks": tasks
    }
    # for item in tasks: print(item.priority.name_priority)
    # for item in tasks: print(item.done)
    return render_template("public/index.html", **context)

@public_bp.route('/edit/task/<int:id_task>/<flag>/', methods=['GET', 'POST'])
@public_bp.route('/edit/task/<int:id_task>/', methods=['GET', 'POST'])
def edit_task(id_task=None, flag=None):
    task = Task.get_by_id(id_task)
    context = {
        "task": task,
        "categories": Category.get_all(),
        "priorities": Priority.get_all(),
        "flag": True
    }
    if flag:
        try:
            task.title = request.form['title-task']
            task.description = request.form['description-task']
            task.date_create = request.form['date-start-task']
            task.date_todo = request.form['date-end-task']
            task.hour_todo = request.form['hour-task']
            task.done = False
            category = request.form['category-task']
            category = Category.get_by_name(category)
            task.id_cate = category.id
            priority = request.form['priority-task']
            priority = Priority.get_by_name(priority)
            task.id_prio = priority.id
            task.id_user = current_user.id
            db.session.add(task)
            db.session.commit()
            flash('The task has beed modify successfully', 'success')
        except:
            flash("The task don't has beed modify successfully", 'error')
        return redirect(url_for('public.index'))
    return render_template('public/create_task.html', **context)

@public_bp.route('/delete/task/<int:id_task>/')
def delete_task(id_task):
    task = Task.get_by_id(id_task)
    if task is not None:
        # To call the function delete_done_task.
        insert_binnacle(id_task)

        db.session.delete(task)
        db.session.commit()
        flash("The task is deleted", "success")
    else:
        flash("Has been an error...", "error")
    return redirect(url_for('public.index'))

@public_bp.route('/done/task/<int:id_task>/')
def done_task(id_task):
    task = Task.get_by_id(id_task)
    # To call the function delete_done_task.
    insert_binnacle(id_task)
    # Delete from task:
    db.session.delete(task)
    db.session.commit()
    flash("The task has been marcked as done.", "success")
    return redirect(url_for("public.index"))

def insert_binnacle(id_task):
    task = Task.get_by_id(id_task)
    binnacle = Binnacle(id_user=current_user.id, title=task.title, description=task.description, date_create=task.date_create, date_todo=task.date_todo, status=True)
    binnacle.save()

@public_bp.route('/task/history/')
def task_history():
    return render_template('public/task_history.html')

@public_bp.route('/user/account/', methods=['GET', 'POST'])
@login_required
def account_user():
    return render_template("public/user_account.html")