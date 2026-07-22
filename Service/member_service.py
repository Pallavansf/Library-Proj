from Repository.member_repository import MemberRepository

class MemberService:

    def __init__(self):
     self.repo_member = MemberRepository()

    def add_member(self, member):
        return self.repo_member.insert(member)

    def get_member(self, memberid):
        return self.repo_member.get(memberid)

    def get_all_members(self):
        return self.repo_member.get_all()

    def update_member(self, member):
        return self.repo_member.update(member)

    def delete_member(self, memberid):
        return self.repo_member.delete(memberid)
    
    def get_member(self,memberid):
        return self.repo_member.get_member(memberid)        

    def is_member_active(self,memberid):
        member = self.repo_member.get_member(memberid)   
        
        if not member:
          return False

        return member._active

    def can_borrow(self,memberid):
      member = self.repo_member.get_member(memberid) 
      if not member:
        return False  
      
      if not bool(member._active):
         return False
      
      if not (member._membershiptype):
          return False
      
      return True
      