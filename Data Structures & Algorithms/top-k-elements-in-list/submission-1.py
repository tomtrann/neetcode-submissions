class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      hashmap = {}

      for n in nums: 
        hashmap[n] = hashmap.get(n,0) + 1
    
      maxheap = []
      for num, freq in hashmap.items():
        maxheap.append((-freq, num))
    
      heapq.heapify(maxheap)
      res = []
      for i in range(k):
        freq, num = heapq.heappop(maxheap)
        res.append(num)

      return res