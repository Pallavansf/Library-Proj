from datetime import date

class Loan:

    def __init__( self, LoanID, BookID, MemberID, BorrowDate, DueDate, ReturnDate=None, Status="BORROWED" ):
      self._loanid = LoanID
      self._bookid = BookID
      self._memberid = MemberID
      self._borrowdate = BorrowDate
      self._duedate = DueDate
      self._returndate = ReturnDate
      self._status = Status

    def __str__ (self):
      return(
        f"Loan id : {self._loanid}\n"
        f"Book id : {self._bookid}\n"
        f"Member id : {self._memberid}\n"
        f"Borrow Date : {self._borrowdate}\n"
        f"Due Date : {self._duedate}\n"
        f"Return Date : {self._returndate}\n"
        f"Status : {"yes" if self._status else "No"}\n"
      )

    def mark_returned(self, returndate):
       if not self._returndate:
        self._returndate = returndate
        self._status = 'RETURNED' 
        return True        

    def mark_overdue(self):
       if self._status == 'BORROWED':          
        if self._duedate < date.today():
          self._status = 'OVERDUE'   
          return True
        return False

    def extend_due_date(self,newduedate):
       self._duedate = newduedate