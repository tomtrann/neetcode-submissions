from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        for i in strs:
            sorted_str = tuple(sorted(i))
            hashmap[sorted_str].append(i)
        
        for value in hashmap.values():
            result.append(value)
        
        return result