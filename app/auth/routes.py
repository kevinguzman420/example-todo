from flask import render_template, redirect, url_for, request, flash, g, session
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import login_manager
from .models import User
from . import auth_bp

user_name = None

@auth_bp.before_request
def before_request():
    g.user = current_user
    # print(current_user.username)

@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User.get_by_email(email)
        if user is not None:
            message = 'This email, {email} already exist.'
            flash(message, 'warning')
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            message = 'User has been saved'
            flash(message, 'success')
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.index')
            return redirect(next_page)
        print("enter")
    return render_template("auth/signup.html", form=True)

@auth_bp.route('/signin/', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    message = None
    if request.method == 'POST':
        print('entro')
        email = request.form['email']
        password = request.form['password']
        user = User.get_by_email(email)
        if user is not None and user.check_password(password):
            message = 'Welcome back {0}'.format(user.username)
            print(user.username)
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.index')
            flash(message, 'success')
            return redirect(next_page)
        else:
            message = 'The datas are invalids'
        flash(message, 'error')
    return render_template("auth/signin.html", form=False)

@auth_bp.route('/logout/')
@login_required
def logout():
    username = User.get_by_id(current_user.id)
    logout_user()
    user_name = "hello"
    flash('See you son {0}'.format(username.username), 'success')
    return redirect(url_for('public.index'))

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))