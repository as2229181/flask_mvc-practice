from flask import render_template,request
from app.models.user import create,User2,update,destory_
import sqlalchemy 
class views:
    def index():#render html網頁出來
        return render_template("users/index.html")#使用 render_template 把templates 內的user/index.html 印出呈現畫面
    
    def news():
        return render_template("users/new.html")
    
    def create():#接受到資料 把資料處存到sql 
        username= request.form["username"]
        email=request.form["email"]
        create(username,email)
        #call mdoels 在models 新增user.py
        return "create successfull"
    def show(id):
        user=User2.query.filter_by(id=id).first()
        return render_template("users/show.html", user=user)
    def edit(id,url_delete,url_update):
        user=User2.query.filter_by(id=id).first()
        return render_template("users/edit.html",user=user,url_delete= url_delete,url_update=url_update)
    def update(id):
        email= request.form["email"]
        update(id,email)
        return "user update successfull"
    def destory(id):
        destory_(id)
        return 