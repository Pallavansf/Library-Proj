class Member:

 def __init__(self, MemberID, MemberName, Age, Phone, Email, MembershipType,IsActive=True):
    self._memberid = MemberID
    self._membername = MemberName
    self._age = Age
    self._phone = Phone
    self._email = Email
    self._membershiptype = MembershipType
    self._active = IsActive

 def update_contact(self, newphone, newemail):
  if self._active:
    self._phone = newphone
    self._email = newemail
    print(f"Contact has been updated")
    return True

 def upgrade_membership(self,newmemtype):
   if self._membershiptype == newmemtype:
    print("Already using this membership.")
    return False
   
   if self._active:
     self._membershiptype = newmemtype
     print(f"Membership has been updated {self._membershiptype}")
     return True
   return False
     

 def activate(self):
   if self._active:
     print(f"Already active")
     return False
   else:
     self._active = True
     print(f"Made active")
     return True

 def deactivate(self):
   if not self._active:
     print(f"Already inactive")
     return False
   else:
     self._active = False
     print(f"Made inactive")
     return True