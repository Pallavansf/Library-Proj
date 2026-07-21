from Entity.member import Member
from Database.connection_manager import DBManager

class MemberRepository:

    def __init__(self):
      self.dbm = DBManager()

    def insert(self, member):
        self.dbm.cursor.execute(
         """
         INSERT INTO MEMBER (MemberID, MemberName, Age, Phone, Email, MembershipType, IsActive )
         VALUES (?,?,?,?,?,?,?)
         """,
            (member._memberid,
             member._membername,
             member._age,
             member._phone,
             member._email,
             member._membershiptype,
             int(member._active))
             )
        self.dbm.commit()
        return True

    def get(self, memberid):
        self.dbm.cursor.execute(
            """
          SELECT * FROM MEMBER WHERE MemberID = ?
            """,(memberid,)
        )
        curmem = self.dbm.cursor.fetchone()
        if curmem:            
             member = Member(
                 MemberID = curmem[0], 
                 MemberName = curmem[1], 
                 Age = curmem[2], 
                 Phone = curmem[3], 
                 Email = curmem[4], 
                 MembershipType = curmem[5],
                 IsActive = bool(curmem[6])
              )
             return member
        return None

    def get_all(self):
        memlist = []
        self.dbm.cursor.execute(
            """
            SELECT * FROM MEMBER 
            """
        )
        curmems = self.dbm.cursor.fetchall()
        if curmems:
          for j in curmems:
           members = Member(
           MemberID = j[0], 
           MemberName = j[1], 
           Age = j[2], 
           Phone = j[3], 
           Email = j[4], 
           MembershipType = j[5],
           IsActive = bool(j[6]))
          
           memlist.append(members)
          return memlist     
        
        else:
         return []    
             

    def update(self, member):
     self.dbm.cursor.execute(
            """
            UPDATE MEMBER SET MemberName = ?, Age = ?, Phone = ?, Email = ?, MembershipType = ?, IsActive = ? 
            WHERE MemberID = ?
            """,
            (member._membername,
             member._age,
             member._phone,
             member._email,
             member._membershiptype,
             int(member._active),
             member._memberid))
     self.dbm.commit()
                  
     return True

    def delete(self, memberid):
     self.dbm.cursor.execute(
        """
        DELETE FROM MEMBER WHERE MemberID = ?
        """,(memberid,))   
     self.dbm.commit()
     return True  