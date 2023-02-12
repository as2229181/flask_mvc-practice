from flask import Flask
from flask import render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)
app.config.from_object("config")
db=SQLAlchemy()
db.init_app(app)
#定義一個class去儲存資料
class User2(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),primary_key=True)
    email=db.Column(db.String(120),primary_key=True)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if(request.method=="POST"):
        username=request.form["username"]
        email=request.form["email"]
        user= User2(id=1, username=username,email=email)
        db.session.add(user)
        db.session.commit()
        return "update"
    else:    
        return render_template("test.html")


@app.route("/hello")
def hello():
    return "hello flask"

@app.route("/hello/<username>")
def hello_user(username):
    return "hello"+username

@app.route("/hello/<int:userid>")
def hello_userid(userid):
    return "hello"+str(userid)

app.run(debug=True)
