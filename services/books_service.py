from models import db, Books

def create_book(title, author, summary):
    book = Books(title=title, author=author, summary=summary)
    db.session.add(book)
    db.session.commit()
    return book

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

def delete_book(book_id):
    book = Books.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    return False

def get_book_by_title(title):
    return Books.query.filter_by(title=title).first()

def get_book_by_author(author):
    return Books.query.filter_by(author=author).all()


    