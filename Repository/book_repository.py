from Database.connection_manager import DBManager
from Entity.book import Book

class BookRepository:

 def __init__ (self):
  self.dbm = DBManager()

 def insert(self,book):
  self.dbm.cursor.execute(
   """
   insert into BOOK
   (BookID, Title, Author, Category, ISBN, PublishedYear, CopiesAvailable, IsActive)
   values (?,?,?,?,?,?,?,?)
   """,
   (book._bookid,
    book._title,
    book._author,
    book._category,
    book._isbn,
    book._publishedyear,
    book._copiesavl,
    int(book._active)))
  
  self.dbm.commit()
  return True

 def get(self,bookid):
  self.dbm.cursor.execute(
   """
   SELECT * FROM BOOK WHERE BookID = ?
   """,(bookid,))
  curval =self.dbm.cursor.fetchone()
  if curval:
   book = Book(
    BookID = curval[0], 
    Title = curval[1], 
    Author = curval[2], 
    Category= curval[3], 
    ISBN=curval[4], 
    PublishedYear = curval[5], 
    CopiesAvailable = curval[6],
    IsActive = bool(curval[7])
   )
   return book


 def get_all(self):
  Bookes = []
  self.dbm.cursor.execute(
   """
   SELECT * FROM BOOK
   """)
  multicurval = self.dbm.cursor.fetchall()
  if multicurval:
    for j in multicurval:
     books =Book(
      BookID = j[0],
      Title=j[1],
      Author=j[2],
      Category=j[3],
      ISBN=j[4],
      PublishedYear=j[5],
      CopiesAvailable=j[6],
      IsActive=bool(j[7])
     ) 
     Bookes.append(books)
    return Bookes
  return [] 

 def update(self,book):
  self.dbm.cursor.execute(
   """
   UPDATE BOOK SET 
    Title = ?, Author = ?, Category = ?, ISBN = ?, PublishedYear = ?, CopiesAvailable = ?, IsActive = ?
   where BookID = ?
   """,
   (book._title,
    book._author,
    book._category,
    book._isbn,
    book._publishedyear,
    book._copiesavl,
    int(book._active),(book._bookid) 
  ))
  self.dbm.commit()
  return True
  
 def delete(self,bookid):
  self.dbm.cursor.execute(
   """
   DELETE FROM BOOK WHERE BookID =?
   """,(bookid,)
   )
  self.dbm.commit()
  return True

 def getbook_name(self,bookname):
   search_pattern = f"%{bookname}%"
   self.dbm.cursor.execute(
    """
    SELECT * FROM BOOK WHERE Title LIKE ?
    """,(search_pattern,)
   )

   get_books = self.dbm.cursor.fetchall()
   booklist_ =[]
   if get_books:
    for j in get_books:
     bookslist = Book (
      BookID = j[0],
      Title=j[1],
      Author=j[2],
      Category=j[3],
      ISBN=j[4],
      PublishedYear=j[5],
      CopiesAvailable=j[6],
      IsActive=bool(j[7])
     )
     booklist_.append(bookslist)
    return booklist_

