from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for i in nums:
            if hashmap[i] > 0:
                return True
            hashmap[i] += 1
        
        return False
        
