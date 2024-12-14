from models import db, myUser

class UserService:
    
    @staticmethod
    def create_user(name, email):
        user = myUser(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_user_by_id(user_id):
        return myUser.query.get(user_id)
    
    @staticmethod
    def get_user_by_email(email):
        return myUser.query.filter_by(email=email).first()

    @staticmethod
    def update_user(user_id, name=None, email=None):
        user = myUser.query.get(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            db.session.commit()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = myUser.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_users():
        return myUser.query.all()
