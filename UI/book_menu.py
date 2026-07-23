from Service.library_services import BookService
from Entity.book import Book

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
  Title = input("Enter the book title : ") 
  Author = input ("Enter the book Author : ")
  Category = input ("Enter the book Categoty : ")
  ISBN = int(input ("Enter the ISBN : "))
  PublishedYear = int(input ("Enter the Publication Year : "))
  CopiesAvailable = int(input ("Enter the Enter the number of copy : "))

  book = Book(BookID,Title,Author,Category,ISBN,PublishedYear, CopiesAvailable)

  return book

 def bookchoose_option(self):
  
  while True:
   
   print(self.bookmenus())

   choice = input("\nChoose the following option: ")

   if choice == "1":
    book_input = self.validate_addbook()
    if book_input:
     result = self.libserv.add_book(book_input)     
     print(result.message)     
    continue   

   elif choice == "2":
    list_book = self.libserv.get_book(int(input("Enter a book id")))
    print(list_book.message)
    if list_book.success:
     print(list_book.data)
     continue
     
   elif choice == "3":
    list_books = self.libserv.get_all_books()
    if list_books.success:
     for book in list_books.data:
        print(book)
        print("-" * 50)
     continue

   elif choice == "4":
    update_book = self.validate_addbook()
    result = self.libserv.update_book(update_book)
    print(result.message)
    continue
   
   elif choice == "5":
    result = self.libserv.delete_book(int(input("Enter the book id to remove")))
    print(result.message)   
    continue
   
   elif choice == "6":
    list_book = self.libserv.search_book(input("Enter a book name"))
    print(list_book.message)

    if list_book.success:
      print(list_book.data)
    continue    

   elif choice == "7" or choice == "EXIT":
    print(f"Returning to Main Menu")
    break
   
   else:
    print(f"Enter an Valid Option from the menu")  


from Service.member_service import MemberService
from Entity.member import Member

class MemberMenu:

 Memserv = MemberService()

 def bookmenus(self):
   self.printbookmenu =  """# MEMBER MANAGEMENT
                            # 1. Add Member
                            # 2. View Member
                            # 3. View All Members
                            # 4. Update Member
                            # 5. Delete Member
                            # 6. Back"""
   return self.printbookmenu

 def adding_themember(self):
   MemberID = int(input("Enter the member id : "))
   MemberName =input("Enter the member Name : ")
   Age = int(input("Enter the Age : "))
   Phone = int(input("Enter the Phone number : "))
   Email = input("Enter the Email : ")
   MembershipType= input("Enter the Membership type : ")

   member = Member(MemberID, MemberName,Age,Phone,Email,MembershipType)
   return member

 def Member_chooseOption(self):

   while True:

    print(self.bookmenus())  
    
    choice = input("\nChoose the following option: ")

    if choice == "1":
     member_input = self.adding_themember()
     if member_input:
      result = self.Memserv.add_member(member_input)     
      print(result.message)     
     continue 

    elif choice == "2":
     member_input = int(input("Enter a Member id to find : "))
     member_search = self.Memserv.get_member(member_input)
     if member_search:
      print(member_search.data)
      print("-" * 50)    
      continue
     
    elif choice == "3":
     members_out = self.Memserv.get_all_members()
     if members_out.success:
      for j in members_out.data:
       print(j)
       print('-' * 50)
     continue

    elif choice == "4":
      member_input = self.adding_themember()
      if member_input:
       update_member = self.Memserv.update_member(member_input)
       print(update_member.message)
      continue

    elif choice == "5":
     mem_input = int(input("Enter the ID to delete"))
     delete_member = self.Memserv.delete_member(mem_input)
     if delete_member.success:
      print(delete_member.message)
     continue

    elif choice == "6" or choice == 'EXIT':
     break
    
    else:
     print("Invalid option.")

from Service.loan_service import LoanService
from Entity.loan import Loan
 
class LoanMenu:
 
 loanserv = LoanService()
 
 def validate_loanentry(self):
  LoanID = int(input("Enter the Loan Id : "))   
  BookID = int(input("Enter the Book Id : "))   
  MemberID  = int(input("Enter the Member Id : "))   
  BorrowDate =  input("Enter Borrow Date : ")
  DueDate = input("Enter the DueDate : ")

  loanentry = Loan(LoanID, BookID , MemberID, BorrowDate, DueDate)
  return loanentry
 
 def bookmenus(self):
   self.printbookmenu =  """# LOAN MANAGEMENT
                            # 1. Borrow Book
                            # 2. Return Book
                            # 3. Renew Loan
                            # 4. View Loan
                            # 5. Member Loans
                            # 6. Book Loans
                            # 7. Overdue Loans
                            # 8. Back"""
   return self.printbookmenu
 
 def Loan_chooseOption(self):

  while True:
   
   print(self.bookmenus())

   choice = input("\nChoose the following option: ")
   
   if choice == "1":
    loan_entry = self.validate_loanentry()
    if loan_entry:
     loan_res = self.loanserv.borrow_book(loan_entry)    
     print(loan_res.message)
     continue

   elif choice == "2":
    loan_input = int(input("Enter an loan id to return : "))
    loan_return = self.loanserv.return_book(loan_input)
    if loan_return.success:
      print(loan_return.message)
    continue
   
   elif choice == "3":
    loan_input = int(input("Enter an loan id to renew : "))
    loan_return = self.loanserv.renew_loan(loan_input)
    if loan_return.success:
      print(loan_return.message)
    continue
   
   elif choice == "4":
    loan_input = int(input("Enter an loan id to search : "))
    loan_return = self.loanserv.get_loan(loan_input)
    if loan_return.success:
      for j in loan_return.data:
       print(j)
       print('-' * 50)
    continue   
   
   elif choice == "5":
    loan_input = int(input("Enter an Member id to search : "))
    loan_return = self.loanserv.get_member_loans(loan_input)
    if loan_return.success:
      for j in loan_return.data:
       print(j)
       print('-' * 50)
    continue 

   elif choice == "6":
    loan_input = int(input("Enter an book id to search : "))
    loan_return = self.loanserv.get_book_loans(loan_input)
    if loan_return.success:
      for j in loan_return.data:
       print(j)
       print('-' * 50)
    continue    
   
   elif choice == "7":
    loan_return = self.loanserv.get_overdue_loans()
    if loan_return.success:
       for j in loan_return.data:
        print(j)
        print('-' * 50)
    continue     

   elif choice == "8" or choice=='EXIT':
    break
   
   else: 
     print("Invalid option.")
   
from Service.loan_service import LoanService
from Entity.loan import Loan

class LoanReport:

 loanserv = LoanService()
 Memserv = MemberService()
 libserv = BookService()

 def bookmenus(self):
   self.printbookmenu =  """# REPORTS
                            # 1. All Books
                            # 2. All Members
                            # 3. Overdue Books
                            # 4. Exit"""
   return self.printbookmenu

 def Report_chooseOption(self):

  while True:
   
   print(self.bookmenus())

   choice = input("\nChoose the following option: ")
   
   if choice == "1": 
    list_books = self.libserv.get_all_books()
    if list_books.success:
     for book in list_books.data:
        print(book)
        print("-" * 50)
     continue

   elif choice == "2":
     members_out = self.Memserv.get_all_members()
     if members_out.success:
      for j in members_out.data:
       print(j)
       print('-' * 50)
     continue

   elif choice == "3":
     loan_return = self.loanserv.get_overdue_loans()
     if loan_return.success:
       for j in loan_return.data:
        print(j)
        print('-' * 50)
     continue     

   elif choice == "4" or choice=='EXIT':
     break
   
   else: 
      print("Invalid option.")

if __name__ == "__main__":
    menu = BookMenu()
    menu.bookchoose_option()