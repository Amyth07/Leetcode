class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = window_sum = nums[0]
        
        for i in range(1, len(nums)):
            window_sum += nums[i] 
            
            if nums[i] > window_sum: # To include the number in current window or not
                window_sum = nums[i]
            
            max_sum = max(max_sum, window_sum) # Keeping track of all windows.
        
        return max_sum
        
