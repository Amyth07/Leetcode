class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_ = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                count += 1
            else:
                count = 0
                
            max_ = max(count, max_)
        
        return max_
    
