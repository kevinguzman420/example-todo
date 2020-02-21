from flask import render_template
from . import auth_bp

@auth_bp.route('/signup/')
def signup():
    return render_template("auth/signup.html", form=True)

@auth_bp.route('/signin/')
def signin():
    return render_template("auth/signin.html", form=False)