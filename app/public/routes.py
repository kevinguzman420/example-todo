from flask import render_template
# from .forms import PostForm
import json

from . import public_bp

@public_bp.route('/')
def index():
    context = {
        "dato1": 1,
        "dato2": 2,
        "dato3": "Gracias Papá Dios!",
        "dato4": "domps"
    }
    return render_template("public/index.html", variable=json.dumps(context))

@public_bp.route('/create/task/', methods=['GET', 'POST'])
def create_task():
    return render_template("public/create_task.html")

@public_bp.route('/user/account/', methods=['GET', 'POST'])
def account_user():
    # form = PostForm()
    return render_template("public/user_account.html")