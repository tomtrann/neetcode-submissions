
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      hashmap = {}
      for i in nums:
        hashmap[i] = hashmap.get(i, 0) + 1
      
      maxheap = []
      for num, freq in hashmap.items():
        maxheap.append((-freq, num))
      
      heapq.heapify(maxheap)
      arr = []

      for i in range(k):
        freq, num = heapq.heappop(maxheap)
        arr.append(num)
      
      return arr