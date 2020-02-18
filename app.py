from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup/')
def signup():
    return render_template("signup.html", form=True)

@app.route('/signin/')
def signin():
    return render_template("signin.html", form=False)

if __name__ == '__main__':
    app.run(port=5000, debug=True)