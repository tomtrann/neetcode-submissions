class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:   
        maxlength = 0
        length = 0

        for i in nums:
            if i == 1: 
                length += 1 
            else: 
                length = 0
            maxlength = max(length, maxlength) 
        return maxlength
            

        