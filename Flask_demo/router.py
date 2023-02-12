from  app import app #引入自己寫完的app package
from flask import render_template,url_for
from app.views.user import views#import 路徑 app->views->user->class views
#router主要負責路徑

@app.route('/',methods=["GET"])
def index(): #請求index出現相對應的頁面
    return  views.index()

@app.route("/new", methods=["GET"])
def new():
    return views.news()

@app.route("/create",methods=["POST"]) #當後臺收到資料先跑到這個/creat路徑再透過函數把資料給creat去處理
def create():
    return views.create()

@app.route("/<int:id>/edit", methods=["GET"]) #顯示資訊以及編輯，所以後墜帶有edit 之後可能會有edit render_template
def edit(id):
    url_delete=url_for("destory",id=id) #處理delete路徑鎖死問題， 在edit頁面就處理
    url_update=url_for("update",id=id)
    return views.edit(id,url_delete=url_delete,url_update=url_update)

@app.route("/<int:id>",methods=["POST"])
def update(id):
    return views.update(id)

@app.route("/<int:id>/delete",methods=["POST"])
def destory(id):
    views.destory(id)
    return "user deleted"
@app.route("/<int:id>",methods=["GET"])
def show(id):
    return views.show(id)    



app.run(debug=True)
