from models import db, ReadingList

class ReadingListService:
    
    @staticmethod
    def add_to_reading_list(user_id, book_name, status=None, rating=None, total_chapters=None, chapters_read=0, comments=None):
        reading_list_item = ReadingList(
            user_id=user_id,
            book_name=book_name,
            status=status,
            rating=rating,
            total_chapters=total_chapters,
            chapters_read=chapters_read,
            comments=comments
        )
        db.session.add(reading_list_item)
        db.session.commit()
        return reading_list_item
    
    @staticmethod
    def get_reading_list_by_user(user_id):
        return ReadingList.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_reading_list_by_id(reading_list_id):
        return ReadingList.query.get(reading_list_id)
    
    @staticmethod
    def update_reading_list(reading_list_id, book_name=None, status=None, rating=None, total_chapters=None, chapters_read=None, comments=None):
        reading_list_item = ReadingList.query.get(reading_list_id)
        if reading_list_item:
            if book_name:
                reading_list_item.book_name = book_name
            if status:
                reading_list_item.status = status
            if rating is not None:
                reading_list_item.rating = rating
            if total_chapters is not None:
                reading_list_item.total_chapters = total_chapters
            if chapters_read is not None:
                reading_list_item.chapters_read = chapters_read
            if comments:
                reading_list_item.comments = comments
            db.session.commit()
            return reading_list_item
        return None

    @staticmethod
    def delete_reading_list(reading_list_id):
        reading_list_item = ReadingList.query.get(reading_list_id)
        if reading_list_item:
            db.session.delete(reading_list_item)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_reading_lists():
        return ReadingList.query.all()
