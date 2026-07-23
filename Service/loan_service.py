from Repository.book_repository import BookRepository
from Repository.member_repository import MemberRepository
from Repository.loan_repository import LoanRepository
from Entity.loan import Loan
from datetime import datetime,timedelta
from Service.Message import ServiceResult
from Service.library_services import BookService
from Service.member_service import MemberService

class LoanService:

    def __init__(self):        
        self.loan_repo = LoanRepository()
        self.member_service = MemberService()
        self.library_service = BookService()

    def borrow_book(self, memberid, bookid):
      borrow_date = datetime.today()
      due_date = borrow_date + timedelta(days=15)            


      if not self.member_service.can_borrow(memberid):
          return ServiceResult(
          success=False,
         message="Member is inactive."
          )

      if not self.library_service.is_book_available(bookid):
         return ServiceResult(
            success=False,
           message="Book is not available for borrowing."
        )
      
      if not self.library_service.decrease_available_copies(bookid):
          return ServiceResult(
              success= False, message= "No available copy to be issued"
          )
       
      borrow_trans = Loan(None, bookid, memberid, borrow_date, due_date, ReturnDate=None, Status="BORROWED")
     
      if not self.loan_repo.insert(borrow_trans):
       self.library_service.increase_available_copies(bookid)
       return ServiceResult(
        success=False,
       message="Transaction Failed & book returned to the library."
)
      return ServiceResult(
      success=True,
       message="Requested book is issued", data = borrow_trans
)

    def return_book(self, loanid):

     loan = self.loan_repo.get(loanid)

     if not loan:
        return ServiceResult(
            success=False,
            message="Check the loan id."
        )

     if loan._status == "RETURNED":
        return ServiceResult(
            success=False,
            message="This loan has already been settled."
        )

     return_date = datetime.today()
     fine = 0     
     FINE_PER_DAY = 15

     if return_date > loan._duedate:
        overdue_days = (return_date - loan._duedate).days
        fine = overdue_days * FINE_PER_DAY

     loan._returndate = return_date
     loan._status = "RETURNED"

     self.loan_repo.update(loan)
     self.library_service.increase_available_copies(loan._bookid)

     return ServiceResult(
        success=True,
        message="Book returned successfully.",
        data=fine
     )    
              

    def get_loan(self, loanid):
     loan = self.loan_repo.get(loanid)

     if not loan:
        return ServiceResult( success=False, message="Loan not found." )

     return ServiceResult( success=True, message="Loan retrieved successfully.", data=loan )
    
    def get_member_loans(self, memberid):
     member = self.member_service.get_member(memberid)

     if not member.success:
      return ServiceResult( success=False, message="Member not found.")

     loans = self.loan_repo.get_member_loans(memberid)

     return ServiceResult( success=True, message="Member loans retrieved successfully.", data=loans )

    def get_book_loans(self, bookid):
        book_avl = self.library_service.get_book(bookid)
        
        if not book_avl:
         return ServiceResult( success=False, message="Book not found." )
        
        book_loan = self.loan_repo.get_book_loans(bookid)
        if book_loan:
          return ServiceResult( success=True, message="Book Loan found.", data= book_loan)
     
        return ServiceResult( success=False, message="Book Loan not found.", data = [])

    def get_overdue_loans(self):
        overdue_loans = self.loan_repo.get_overdue_loans()
        if not overdue_loans:
          return ServiceResult( success=False, message="Overdues not found.",data =[] )
             
        return ServiceResult( success=True, message="Overdues found.", data= overdue_loans)
    
    def renew_loan(self, loanid):

     loan_result = self.get_loan(loanid)

     if not loan_result.success:
        return loan_result

     loan = loan_result.data

     if loan._status == "RETURNED":
        return ServiceResult(
            success=False,
            message="Returned loans cannot be renewed."
        )

     if not self.member_service.can_borrow(loan._memberid):
        return ServiceResult(
            success=False,
            message="Member is not eligible for renewal."
        )
     LOAN_DAYS = 15

     loan._duedate += timedelta(days=LOAN_DAYS)

     self.loan_repo.update(loan)

     return ServiceResult(
        success=True,
        message="Loan renewed successfully.",
        data=loan
      )
 

