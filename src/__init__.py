from flask import Flask, session, render_template, request, redirect, url_for
from flask_material import Material
from bson.json_util import dumps
import json
from bson.objectid import ObjectId
from .connections import usercoll, blogcoll, secret_keys
from .models import users, blogs
from werkzeug.security import generate_password_hash, check_password_hash

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)

app.secret_key = secret_keys

app.json_encoder = JSONEncoder

Material(app)

@app.route("/")
def index():
    # session.pop('user', None)
    return render_template("home.html")

@app.route("/blog")
def blog():
    if 'user' in session:
        return render_template("blog.html", user=session["user"])
    else:
        return redirect(url_for("login"))

# login
@app.route("/login")
def login():
    return render_template("auth/login.html")

# login process
@app.route("/loginpost", methods=['POST'])
def loginpost():
    email = request.form['email']
    password = request.form['password']

    emailCheck = usercoll.find_one({"email" : email})

    if emailCheck != None:
        pwhash = emailCheck["password"]
        if check_password_hash(pwhash, password):
            session['user'] = emailCheck
            return redirect(url_for("blog"))
        else:
            return "gagal login"
    else:
        session['message'] = "login was fails, please check your email or password"
        return redirect(url_for("login"))

# register
@app.route("/register")
def register():
    return render_template("auth/register.html")

# register process
@app.route("/registerpost", methods=['POST'])
def registerpost():
    username = request.form['firstname'] + " " + request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    pwhash = generate_password_hash(password, "sha256")

    regist = usercoll.insert_one(users(username, email, pwhash))
    
    user = usercoll.find_one({"email" : email})

    session['user'] = user
    return redirect(url_for("blog"))


@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))


if(__name__ == "__main__"):
    app.run()