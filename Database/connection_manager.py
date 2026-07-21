import sqlite3

class DBManager:
 
  def __init__ (self):
   self.conn = sqlite3.connect("Database/Library.db")
   self.cursor = self.conn.cursor()
   self.cursor.execute("PRAGMA foreign_keys = ON")

  def commit(self):
   self.conn.commit()   

  def rollback(self):
   self.conn.rollback()
   print(f"Rollback success")

  def close(self):
    self.conn.close()

  def create_table(self):
   self.cursor.execute(
   """
   CREATE TABLE IF NOT EXISTS BOOK (
    BookID          INTEGER PRIMARY KEY,
    Title           TEXT NOT NULL,
    Author          TEXT NOT NULL,
    Category        TEXT NOT NULL,
    ISBN            TEXT UNIQUE NOT NULL,
    PublishedYear   INTEGER NOT NULL,
    CopiesAvailable INTEGER NOT NULL,
    IsActive        INTEGER NOT NULL CHECK (IsActive IN (0, 1))
   ); """)
    
   self.cursor.execute(
   """
    CREATE TABLE IF NOT EXISTS MEMBER( 
    MemberID        INTEGER  Primary Key ,
    MemberName      TEXT     NOT NULL,   
    Age             INTEGER  NOT NULL ,  
    Phone           TEXT     NOT NULL,    
    Email           TEXT     UNIQUE NOT NULL,      
    MembershipType  TEXT     NOT NULL,    
    IsActive        INTEGER  NOT NULL CHECK (IsActive IN (0, 1)));    
    """)
   
   self.cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS LOAN( 
    LoanID      INTEGER Primary Key,          
    BookID      INTEGER NOT NULL,
    MemberID    INTEGER NOT NULL,
    BorrowDate  TEXT NOT NULL,             
    DueDate     TEXT NOT NULL ,            
    ReturnDate  TEXT,                 
    Status      TEXT NOT NULL CHECK (Status IN ('BORROWED','RETURNED','OVERDUE')),
    FOREIGN KEY (BookID) REFERENCES BOOK (BookID),
    FOREIGN KEY (MemberID) REFERENCES MEMBER (MemberID))
    """)
   self.commit()

    