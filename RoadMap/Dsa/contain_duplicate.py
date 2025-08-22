class Solution:
    
    def containsDuplicate(self, nums:List[num])->bool:
        
        seen:Set() = ()
        
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False
