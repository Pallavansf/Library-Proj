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