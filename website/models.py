from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#These two objects follow one to many model - One user is mapped to many notes.

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True)
    firstname = db.Column(db.String(100))
    password = db.Column(db.String(100))
    notes = db.relationship("Note") #mapping one user to many notes
    
class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey("user.id")) #mapping a note to a particular user 
    

    
    