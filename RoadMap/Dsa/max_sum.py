class Solution:
    def max_sum(self,nums:List[int])->int:
        curr_sum:int = nums[0]
        max_sum:int = nums[0]
        
        for num in nums[1:]:
            curr_sum = max(curr_sum, curr_sum+num)
            max_sum = max(max_sum,curr_sum)
        
        return max_sum