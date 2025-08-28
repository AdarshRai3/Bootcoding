class Solution:
    def subarraySum(self, nums:List[int],k:int)->int:
        
        prefix_count  = default_dict(int)
        prefix_count[0]=1
        
        prefix_sum=0
        count = 0
        
        for num in nums:
            prefix_sum += num
            
            if (prefix_sum-k) in prefix_count:
                count += prefix_count[prefix_sum-k]
            
            prefix_count[prefix_sum]+=1
            
        
        return count