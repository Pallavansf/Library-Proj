from Repository.book_repository import BookRepository
from Service.Message import ServiceResult
from Utils import logger

class BookService:
    
    def __init__(self):
        self.repo_book  = BookRepository()

    def add_book(self, book):
     added = self.repo_book.insert(book)

     if not added:
        return ServiceResult(success=False, message="Book could not be added." )

     return ServiceResult(success=True, message="Book added successfully.", data=book )

    def get_book(self, bookid):
        book = self.repo_book.get(bookid)

        if not book:
            return ServiceResult( success=False, message="Book not found.")

        logger.info("Book Added", "ABC123")
        return ServiceResult( success=True, message="Book found.", data=book)

    def get_all_books(self):
        books = self.repo_book.get_all()

        if not books:
            return ServiceResult(success=True, message="No books found.", data=[])
        return ServiceResult( success=True, message="Books retrieved successfully.", data=books)
        
    def update_book(self, book):
        updated = self.repo_book.update(book)

        if not updated:
            return ServiceResult( success=False, message="Book update failed." )

        return ServiceResult( success=True, message="Book updated successfully.", data=book)
        
    def delete_book(self, bookid):
        deleted = self.repo_book.delete(bookid)

        if not deleted:
            return ServiceResult(success=False, message="Book deletion failed." )

        return ServiceResult(success=True, message="Book deleted successfully.")

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

    def search_book(self, bookname):
        book =  self.repo_book.getbook_name(bookname)

        if not book:
            return ServiceResult( success=False, message="Book not found." )

        return ServiceResult( success=True, message="Book found.", data=book)