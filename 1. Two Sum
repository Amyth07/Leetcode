class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        mem = {}
        
        for key, value in enumerate(nums):
            diff = target - value
            
            if diff in mem:
                return [mem[diff], key]
            else:
                mem[value] = key
        
        return []
