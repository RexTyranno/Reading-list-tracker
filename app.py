from flask import Flask, request, jsonify
from models import db, myUser, ReadingLists, rltobooks, Books
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from services.auth_service import authenticate_user, register_user, login_user
from decorators.auth_decorator import token_required
from utils.jwt_utils import generate_jwt

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


@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    name = request.json.get('name')
    
    user = register_user(email, password, name)
    return jsonify({"message": "Registration successful", "user_id":user.id, "user_name":user.name}), 201
   
@app.route('/reading_lists', methods=['GET'])
@token_required
def get_all_reading_lists(user_id):
    reading_lists = ReadingLists.query.filter_by(user_id=user_id).all()
    return jsonify({
        'user_id': user_id,
        'reading_lists': [{'id': rl.id, 'name': rl.name} for rl in reading_lists]
    }), 200   


@app.route('/reading_lists/<int:user_id>', methods=['POST'])
@token_required
def create_reading_list(user_id):
    name = request.json.get('name')
    reading_list = ReadingLists(name=name, user_id=user_id)
    db.session.add(reading_list)
    db.session.commit()
    return jsonify({"message": "Reading list created successfully", "reading_list_id":reading_list.id}), 201

@app.route('/reading_lists/<int:reading_list_id>', methods=['GET'])
@token_required
def get_reading_list(user_id, reading_list_id):
    reading_list = ReadingLists.query.filter_by(id=reading_list_id, user_id=user_id).first()
    return jsonify({"reading_list": reading_list.name}), 200

@app.route('/reading_lists/<int:reading_list_id>', methods=['POST'])
@token_required
def add_book_to_reading_list(user_id, reading_list_id):
    reading_list_id = request.json.get('reading_list_id')
    book_id = request.json.get('book_id')
    status = request.json.get('status')
    
    rltobooks = rltobooks(reading_list_id=reading_list_id, book_id=book_id, status=status)
    db.session.add(rltobooks)
    db.session.commit()

@app.route('/reading_lists/<int:reading_list_id>', methods=['POST'])
@token_required
def delete_book_from_reading_list(user_id, reading_list_id):
    reading_list_id = request.json.get('reading_list_id')
    book_id = request.json.get('book_id')
    
    rltobooks = rltobooks.query.filter_by(reading_list_id=reading_list_id, book_id=book_id).first()
    db.session.delete(rltobooks)
    db.session.commit()
    return jsonify({"message": "Book deleted from reading list successfully"}), 200



if __name__=='__main__':
    app.run(debug=True)