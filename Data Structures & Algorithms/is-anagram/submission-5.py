class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmaps = {} 
        hashmapt = {}
        
        for i in range(len(s)):
            hashmaps[s[i]] = hashmaps.get(s[i], 0) + 1
            hashmapt[t[i]] = hashmapt.get(t[i],0) + 1

        for n in hashmaps:
            if hashmaps[n] != hashmapt.get(n, 0):
                return False
        return True