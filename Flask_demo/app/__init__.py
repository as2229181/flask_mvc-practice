from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)

app.config.from_object('config')
db=SQLAlchemy(app) #把flask傳入SQLAlchemy 進行資料處理



