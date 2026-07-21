from Entity.book import Book
from Repository.book_repository import BookRepository

class BookService:
    
    def __init__(self):
        self.repo_book  = BookRepository()

    def add_book(self, book):
        self.repo_book.insert(book)
        return True

    def get_book(self, bookid):
        return self.repo_book.get(bookid)        

    def get_all_books(self):
        return self.repo_book.get_all()
        
    def update_book(self, book):
        return self.repo_book.update(book)
        
    def delete_book(self, bookid):
        return self.repo_book.delete(bookid)         