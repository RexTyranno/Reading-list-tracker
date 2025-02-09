import jwt
from datetime import datetime, timedelta, timezone
from config import Config
from models import myUser

def generate_jwt(email):
    payload = {
        'email': email,
        'exp': datetime.now(timezone.utc) + timedelta(hours=1)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt(token):
    try:
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
        email = payload['email']
        user = myUser.query.filter_by(email=email).first()
        return user.id
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token 