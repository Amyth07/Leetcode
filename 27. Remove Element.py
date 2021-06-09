# Two Pointer

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_target = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[last_target] = nums[i]
                last_target += 1
        
        return last_target
