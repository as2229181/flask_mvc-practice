#都處理與資料庫有關的事情
from .. import db #..為flask_demo->app 的 __init__.py 裡面有設定db
from sqlalchemy import desc,column,select

class User2(db.Model): #建立一個class儲存用戶資訊
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    username=db.Column(db.String(80),unique=True)
    email=db.Column(db.String(120),unique=True)


def create(username,email): #將資料儲存進入user table中 從request中拿到傳過來 前端 傳到 router 
    if User2.query.count() == 0:
        user=User2(id=1,username=username,email=email)
    else:  
        oldUser = User2.query.order_by(desc('id')).first()
        user=User2(id=oldUser.id+1,username=username,email=email)#再傳到views->create(呈現畫面後)傳到model(處理資料)->存到User(上方的class user)資料結構後給這裡
    db.session.add(user) #寫入db
    db.session.commit()
    return

def update(id,email):
    user=User2.query.filter_by(id=id).first() #利用user2去找到這個id的email
    user.email=email#將email給更新
    db.session.commit()
    return
def destory_(id):
    user=User2.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return



    