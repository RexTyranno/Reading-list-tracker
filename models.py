from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class myUser(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique= True)
    password_hash = db.Column(db.String(128), nullable= False)
    
    def set_password(self, password):
        self.password_hash= generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Books(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    summary = db.Column(db.String(255))
    
class ReadingLists(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('my_user.id'), nullable=False)
    
class rltobooks(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    rl_id = db.Column(db.Integer, db.ForeignKey('reading_lists.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    status = db.Column(db.String(100))
    
    