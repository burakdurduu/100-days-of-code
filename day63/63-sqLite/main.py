# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    tid: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

    def __init__(self, tid, title, author, rating):
        self.tid = tid
        self.title = title
        self.author = author
        self.rating = rating


# Create A New Record ----------------

# new_book = Book(tid=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
# new_book = Book(tid=2, title="Warcraft", author="Blizzard Entertainment", rating=7.2)
# with app.app_context():
#     db.create_all()
#     db.session.add(new_book)
#     db.session.commit()

# Read All Records ------------------

# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()


# Update A Particular Record By Query -------------------

# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()


# Update A Record By PRIMARY KEY --------------------

# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()

# Delete A Particular Record By PRIMARY KEY -------------------------

# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.tid == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
