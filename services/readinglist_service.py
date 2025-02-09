from models import db, ReadingLists

class ReadingListService:
    
    @staticmethod
    def create_reading_list(user_id, reading_list_name):
        reading_list_item = ReadingLists(
            user_id=user_id,
            name=reading_list_name
        )
        db.session.add(reading_list_item)
        db.session.commit()
        return reading_list_item
    
    @staticmethod
    def get_reading_lists(user_id):
        return ReadingLists.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def update_reading_list(reading_list_id, reading_list_name=None):
        reading_list_item = ReadingLists.query.get(reading_list_id)
        if reading_list_item:
            if reading_list_name:
                reading_list_item.name = reading_list_name
            db.session.commit()
            return reading_list_item
        return None

    @staticmethod
    def delete_reading_list(reading_list_id):
        reading_list_item = ReadingLists.query.get(reading_list_id)
        if reading_list_item:
            db.session.delete(reading_list_item)
            db.session.commit()
            return True
        return False
