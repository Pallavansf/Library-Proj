from Repository.member_repository import MemberRepository
from Service.Message import ServiceResult

class MemberService:

    def __init__(self):
     self.repo_member = MemberRepository()

    def add_member(self, member):
        member = self.repo_member.insert(member)

        if not member:
           return ServiceResult(success=False, message="Member not added." )

        return ServiceResult(success=True, message="Member added.", data = member )

    def get_member(self, memberid):
        member = self.repo_member.get(memberid)

        if not member:
          return ServiceResult(success=False, message="Member not Found." )
        
        return ServiceResult(success=True, message="Member Found.", data = member )


    def get_all_members(self):
        members = self.repo_member.get_all()

        if not members:
           return ServiceResult(success=False, message="Members not Found.", data =[] )
                
        return ServiceResult(success=True, message="Members Found.", data = members )

    def update_member(self, member):
        updated = self.repo_member.update(member)

        if not updated:
          return ServiceResult( success=False, message="Member update failed." )

        return ServiceResult( success=True, message="Member updated successfully.", data=member )

    def delete_member(self, memberid):
       deleted = self.repo_member.delete(memberid)

       if not deleted:
         return ServiceResult( success=False, message="Member deletion failed." )

       return ServiceResult( success=True, message="Member deleted successfully.")

    def is_member_active(self,memberid):

     member_result = self.get_member(memberid)
        
     if not member_result.success:
        return member_result

     member = member_result.data
     if not member._active:
        return ServiceResult( success=False, message="Member is inactive.", data=False )

     return ServiceResult(success=True, message="Member is active.", data=True )
    
    def can_borrow(self,memberid):
      member = self.repo_member.get(memberid) 
      if not member:        
        return ServiceResult(success=False, message="No member found.")
      
      if not bool(member._active):         
         return ServiceResult(success=False, message="Inactive member.")      

      if not (member._membershiptype):          
          return ServiceResult(success=False, message="No active Membership.")
      
      return ServiceResult(success=True, message="Member eligible to borrow.", data = member)
      