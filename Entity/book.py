class Book:

 def __init__ (self,BookID, Title, Author, Category, ISBN, PublishedYear, CopiesAvailable, IsActive=True):
    self._bookid =  BookID
    self._title = Title
    self._author =  Author
    self._category =  Category
    self._isbn =  ISBN
    self._publishedyear = PublishedYear
    self._copiesavl =  CopiesAvailable
    self._active = IsActive

 def __str__(self):
   return (
            f"Book ID      : {self._bookid}\n"
            f"Title        : {self._title}\n"
            f"Author       : {self._author}\n"
            f"Category     : {self._category}\n"
            f"ISBN         : {self._isbn}\n"
            f"Published Yr : {self._publishedyear}\n"
            f"Copies Avail : {self._copiesavl}\n"
            f"Active       : {'Yes' if self._active else 'No'}"
        )   

 def borrow_book(self):
    if not self._active:
      print(f"Book '{self._title}' is inactive and cannot be borrowed.")
      return False

    if self._copiesavl <= 0:
      print(f"No copies of '{self._title}' are available.")
      return False

    self._copiesavl -= 1
    print(f"Book '{self._title}' has been issued successfully.")
    return True

 def return_book(self):
  self._copiesavl +=1  
  print(f"the book {self._title} has been returned")
  return True

 def activate(self):
   if not self._active: 
     self._active = True
     print (f"Book {self._title} made active")
     return True
   else:
     print(f"Book is already active")  
     return False

 def deactivate(self):
   if self._active:
     self._active = False
     print (f"Book {self._title} made in active")
     return True
   else:
     print(f"Book is already in active")  
     return False 

 def change_category(self,nwcategory):
   if self._active:
     self._category = nwcategory
     print(f"Category has been updated {self._category} for {self._title}")
     return True

 def update_copies(self, new_copy_count):

    if new_copy_count < 0:
        print("Copies cannot be negative.")
        return False    

    self._copies_available = new_copy_count
    print(f"Copies updated to {self._copies_available} for '{self._title}'.")    
    return True
  