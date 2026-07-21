from Entity.loan import Loan
from Database.connection_manager import DBManager


class LoanRepository:

    def __init__(self):
        self.dbm = DBManager()

    def insert(self, loan):
        self.dbm.cursor.execute(
            """
          INSERT INTO LOAN (LoanID, BookID, MemberID, BorrowDate, DueDate, ReturnDate, Status)
            VALUES(?,?,?,?,?,?,?)
            """,
         (loan._loanid, loan._bookid , loan._memberid, loan._borrowdate , loan._duedate, loan._returndate , loan._status ))
        self.dbm.commit()
        return True

    def get(self, loanid):
        self.dbm.cursor.execute(
            """
           SELECT * FROM LOAN WHERE LoanID =?
             """,(loanid,)
        )
        curloan = self.dbm.cursor.fetchone()
        if curloan:
          single_loan = Loan(
              LoanID = curloan[0], 
              BookID = curloan[1], 
              MemberID = curloan[2], 
              BorrowDate = curloan[3], 
              DueDate = curloan[4], 
              ReturnDate = curloan[5], 
              Status = curloan[6]
          )
          return single_loan
        return None 

    def get_all(self):
       multi_loans = []
       self.dbm.cursor.execute(
         """
         SELECT * FROM LOAN
         """
       )
       curvals = self.dbm.cursor.fetchall()
       if curvals:
        for j in curvals:
         multi_loan = Loan(LoanID = j[0], 
              BookID = j[1], 
              MemberID = j[2], 
              BorrowDate = j[3], 
              DueDate = j[4], 
              ReturnDate = j[5], 
              Status = j[6]           
          )
         multi_loans.append(multi_loan)
        return multi_loans
       return []

    def update(self, loan):
        self.dbm.cursor.execute(
            """
            UPDATE LOAN SET BorrowDate = ?, DueDate = ?, ReturnDate = ?, Status = ?
            WHERE LoanID = ?
             """,
             (loan._borrowdate , loan._duedate, loan._returndate , loan._status, loan._loanid,)
        )
        self.dbm.commit()
        return True

    def delete(self, loanid):
        self.dbm.cursor.execute(
            """
        DELETE FROM LOAN WHERE LoanID = ?
            """ ,(loanid,)
        ) 
        self.dbm.commit()
        return True

    # Additional Query Methods

    def get_member_loans(self, memberid):
      memlist =[]
      self.dbm.cursor.execute(
            """
         SELECT * FROM LOAN WHERE MemberID = ?
            """ ,(memberid,)
        ) 
      memeberexec = self.dbm.cursor.fetchall()
      if memeberexec:
         for j in memeberexec:
            memsloans = Loan(
             LoanID = j[0], 
              BookID = j[1], 
              MemberID = j[2], 
              BorrowDate = j[3], 
              DueDate = j[4], 
              ReturnDate = j[5], 
              Status = j[6])
            memlist.append(memsloans)
         return memlist
      return []
           

    def get_book_loans(self, bookid):     
      book_list= []   
      self.dbm.cursor.execute(
            """
        SELECT * FROM LOAN WHERE BookID = ?
            """ ,(bookid,)
        ) 
      book = self.dbm.cursor.fetchall()      
      if book:
        for j in book:
         bookide = Loan(
           LoanID = j[0], 
           BookID = j[1], 
           MemberID = j[2], 
           BorrowDate = j[3], 
           DueDate = j[4], 
           ReturnDate = j[5], 
           Status = j[6]
         )
         book_list.append(bookide)
        return book_list
      return []
      

    def get_overdue_loans(self,status):
        status_list =[]
        self.dbm.cursor.execute(
            """
        SELECT * FROM LOAN WHERE Status = ?
            """ 
        ,(status,))
        statuses = self.dbm.cursor.fetchall()
        if statuses:
          for j in statuses:
           statobj = Loan(
           LoanID = j[0], 
           BookID = j[1], 
           MemberID = j[2], 
           BorrowDate = j[3], 
           DueDate = j[4], 
           ReturnDate = j[5], 
           Status = j[6]
              )
           status_list.append(statobj)
          return status_list
        return []
            


