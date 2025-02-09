from functools import wraps
from flask import request, jsonify
from utils.jwt_utils import verify_jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        user_id = verify_jwt(token)
        if not user_id:
            return jsonify({'message': 'Token is invalid or expired!'}), 403
        
        return f(user_id, *args, **kwargs)
    
    return decorated 