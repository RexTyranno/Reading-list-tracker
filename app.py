from flask import Flask, request
from models import db, User, ReadingList
from flask_migrate import Migrate

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://avnadmin:AVNS_ghnEugp6FHWRKLhqcnC@pg-a6b31dc-proback-db.j.aivencloud.com:15572/defaultdb?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return "This is a reading list :3"


if __name__=='__main__':
    app.run(debug=True)