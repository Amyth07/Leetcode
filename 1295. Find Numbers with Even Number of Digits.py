class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([ele for ele in nums if len(str(ele)) % 2 == 0])


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for ele in nums:
            if len(str(ele)) % 2 == 0:
                count += 1
        return counta
               
