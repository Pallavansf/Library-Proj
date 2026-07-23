from Service.library_services import BookService
from Entity.book import Book

# ===============================
#  LIBRARY MANAGEMENT SYSTEM
# ===============================

# 1. Book Management
# 2. Member Management
# 3. Loan Management
# 4. Reports
# 5. Exit

class BookMenu:

 libserv = BookService()

 def bookmenus(self):
  self.printbookmenu = """# BOOK MANAGEMENT OPTIONS
                          # 1. Add Book
                          # 2. View Book
                          # 3. View All Books
                          # 4. Update Book
                          # 5. Delete Book
                          # 6. Search Books
                          # 7. Back"""
  return self.printbookmenu

 def validate_addbook(self):
  BookID = int(input("Enter the book id : ")) 
  Title = input("Enter the book title") 
  Author = input ("Enter the book Author")
  Category = input ("Enter the book Categoty")
  ISBN = int(input ("Enter the ISBN"))
  PublishedYear = int(input ("Enter the Publication Year"))
  CopiesAvailable = int(input ("Enter the Enter the number of copy"))

  book = Book(BookID,Title,Author,Category,ISBN,PublishedYear, CopiesAvailable)

  return book

 def bookchoose_option(self):
  
  while True:
   
   print(self.bookmenus())
   choice = input("\nChoose the following option: ")

   if choice == "1":
    self.book_input = self.validate_addbook()
    if self.book_input:
     result = self.libserv.add_book(self.book_input)
     print(result.message)     
    continue   

   elif choice == "2":
    list_book = self.libserv.get_book(int(input("Enter a book id")))
    print(list_book.message)
    if list_book.success:
     print(list_book.data)
     continue
     
   elif choice == "3":
    self.list_books = self.libserv.get_all_books()
    if self.list_books:
     self.list_books

     continue
   elif choice == "4":
    self.update_book = self.validate_addbook()
    self.libserv.update_book(self.update_book)
    print(f"Book has been updated")
    continue
   elif choice == "5":
    self.libserv.delete_book(int(input("Enter the book id to remove")))
    print(f"Book has been removed")
    continue
   elif choice == "6":
    self.list_book = self.libserv.search_book(input("Enter a book name"))
    if self.list_book:
     self.list_book
     continue    
   elif choice == "7" or choice == "EXIT":
    print(f"Returning to Main Menu")
    break
   else:
    print(f"Enter an Valid Option from the menu")  

 

# BOOK MANAGEMENT
# 1. Add Book
# 2. View Book
# 3. View All Books
# 4. Update Book
# 5. Delete Book
# 6. Search Books
# 7. Back

# MEMBER MANAGEMENT
# 1. Add Member
# 2. View Member
# 3. View All Members
# 4. Update Member
# 5. Delete Member
# 6. Back

# LOAN MANAGEMENT
# 1. Borrow Book
# 2. Return Book
# 3. Renew Loan
# 4. View Loan
# 5. Member Loans
# 6. Book Loans
# 7. Overdue Loans
# 8. Back


# REPORTS
# 1. All Books
# 2. All Members
# 3. Overdue Books
# 4. Exit