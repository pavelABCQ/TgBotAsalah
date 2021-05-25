from flask import Flask, redirect, url_for, render_template
from forms import *
from models import *
from flask_wtf import CSRFProtect
from waitress import serve

app = Flask(__name__)

csrf = CSRFProtect(app)
csrf.init_app(app)
app.config['SECRET_KEY'] = "mATVEY IS bROTHER"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/registration", methods = ["GET","POST"])
def registration():
    form = RegForm()
    if form.validate_on_submit():
        return redirect(url_for("profile"))
    return render_template("register.html", form = form)


@app.route("/conacts")
def contacts():
    return render_template("contacts.html")


@app.route("/enter")
def enter():
    return render_template("enter.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/")
def hello():
    return redirect(url_for("main"))


if __name__ == '__main__':
    serve(app, port = 5000, host = "127.0.0.1")
