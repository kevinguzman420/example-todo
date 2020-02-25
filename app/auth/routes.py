from flask import render_template
from .models import User
from . import auth_bp

@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    return render_template("auth/signup.html", form=True)

@auth_bp.route('/signin/', methods=['GET', 'POST'])
def signin():
    
    return render_template("auth/signin.html", form=False)