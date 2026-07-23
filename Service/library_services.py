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

    def is_book_available(self, bookid):
         book= self.repo_book.get(bookid)
         if not book:
             return False
         
         if not book._active:
             return False
         
         if book._copiesavl<=0:
             return False
         
         return True  

    def decrease_available_copies(self,bookid):
        book = self.repo_book.get(bookid)

        if not book:
         return False   
        
        if book._copiesavl <=0:
            return False
        
        book._copiesavl-=1
        return self.repo_book.update(book)
        

    def increase_available_copies(self, bookid):
       book =  self.repo_book.get(bookid)

       if not book:
           return False       
       
       book._copiesavl+=1
       return self.repo_book.update(book)