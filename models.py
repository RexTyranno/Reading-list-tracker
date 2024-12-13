from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique= True)
    
class ReadingList(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_name= db.Column(db.String(512), nullable= False)
    status= db.Column(db.String(100))
    rating= db.Column(db.Float)
    total_chapters= db.Column(db.Integer)
    chapters_read= db.Column(db.Integer)
    comments= db.Column(db.Text)