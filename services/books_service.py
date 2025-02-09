from models import db, Books

class BooksService:
    
    @staticmethod
    def create_book(title, author, summary):
        book = Books(title=title, author=author, summary=summary)
        db.session.add(book)
        db.session.commit()
        return book
    
    @staticmethod
    def update_book(book_id, title=None, author=None, summary=None):
        book = Books.query.get(book_id)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if summary:
                book.summary = summary
            db.session.commit()
            return book
        return None
    
    @staticmethod
    def delete_book(book_id):
        book = Books.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_book_by_title(title):
        return Books.query.filter_by(title=title).first()
    
    @staticmethod
    def get_book_by_author(author):
        return Books.query.filter_by(author=author).all()
    
    
        