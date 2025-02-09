from flask import Flask, request, jsonify
from models import db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from services.auth_service import register_user, login_user
from services.readinglist_service import create_reading_list, get_reading_lists
from decorators.auth_decorator import token_required

load_dotenv()

app= Flask(__name__)

db_connection = os.getenv('DB_CONNECTION')

if not db_connection:
    raise ValueError("No DB_CONNECTION found in environment variables")

app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return "This is a reading list :3"

# AUTHENTICATION ROUTES 
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400
    
    login_response = login_user(email, password)
    if login_response:
        return jsonify(login_response)
    
    return jsonify({'message': 'Invalid credentials'}), 401

# REGISTRATION ROUTES
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    name = request.json.get('name')
    
    user = register_user(email, password, name)
    return jsonify({"message": "Registration successful", "user_id":user.id, "user_name":user.name}), 201

# READING LIST ROUTES
@app.route('/reading_lists', methods=['GET'])
@token_required
def get_all_reading_lists(user_id):
    reading_lists = get_reading_lists(user_id)
    return jsonify({"reading_lists": [{"id": rl.id, "name": rl.name} for rl in reading_lists]}), 200


@app.route('/reading_lists', methods=['POST'])
@token_required
def create_reading_list(user_id):
    name = request.json.get('name')
    reading_list = create_reading_list(user_id, name)
    return jsonify({"message": "Reading list created successfully", "reading_list_id":reading_list.id}), 201

if __name__=='__main__':
    app.run(debug=True)