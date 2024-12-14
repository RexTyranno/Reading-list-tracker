from flask import Flask, request
from models import db, myUser, ReadingList
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

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


if __name__=='__main__':
    app.run(debug=True)