class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s, hashmap_t = {}, {}

        for c in range(len(s)):
            hashmap_s[s[c]] = hashmap_s.get(s[c], 0) + 1
            hashmap_t[t[c]] = hashmap_t.get(t[c], 0) + 1
        
        for i in hashmap_s:
            if hashmap_s[i] != hashmap_t.get(i, 0):
                return False
        
        return True