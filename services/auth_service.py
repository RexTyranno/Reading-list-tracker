from models import db, myUser
from utils.jwt_utils import generate_jwt
from flask import abort
    
def register_user(email, password, name):
    user = myUser(email=email, name=name)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(email, password):
    user = myUser.query.filter_by(email=email).first()
    
    if user and user.check_password(password):
        return user
    else:
        abort(401, description="Invalid email or password")

def login_user(email, password):
    user = authenticate_user(email, password)
    if user:
        token = generate_jwt(user.email)
        return {'token': token, 'user_email': user.email}
    return None