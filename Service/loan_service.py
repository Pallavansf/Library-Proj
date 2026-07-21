from Repository.book_repository import BookRepository
from Repository.member_repository import MemberRepository
from Repository.loan_repository import LoanRepository

class LoanService:

    def __init__(self):
        self.book_repo = BookRepository()
        self.member_repo = MemberRepository()
        self.loan_repo = LoanRepository()

    def borrow_book(self, memberid, bookid):
        pass

    def return_book(self, loanid):
        pass

    def get_loan(self, loanid):
        pass

    def get_member_loans(self, memberid):
        pass

    def get_book_loans(self, bookid):
        pass

    def get_overdue_loans(self):
        pass