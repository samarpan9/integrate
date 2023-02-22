from web_app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String


#class for users table
class User(db.Model):

    __tablename__ = "users"

    client_id           = Column(Integer, primary_key=True)
    email               = Column(String(100))
    password            = Column(String(100))
    username            = Column(String(100))
    status              = Column(String(200))
    created_date        = Column(String(30), default = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])





    










