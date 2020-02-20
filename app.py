from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "dato1": 1,
        "dato2": 2,
        "dato3": "Gracias Papá Dios!",
        "dato4": "domps"
    }
    return render_template("index.html", variable=json.dumps(context))

@app.route('/signup/')
def signup():
    return render_template("signup.html", form=True)

@app.route('/signin/')
def signin():
    return render_template("signin.html", form=False)

@app.route('/create/task/', methods=['GET', 'POST'])
def create_task():
    return render_template("create_task.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)