class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      

      hashmaps = {}
      hashmapt = {}

      for c in range(len(s)):
        hashmaps[s[c]] = hashmaps.get(s[c], 0) + 1
        hashmapt[t[c]] = hashmapt.get(t[c], 0) + 1
      
      for i in hashmaps:
        if hashmaps[i] != hashmapt.get(i, 0):
          return False
      
      return True