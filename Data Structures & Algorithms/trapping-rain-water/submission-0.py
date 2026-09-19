class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        l = 0                                 #   l               r
        r = len(height) - 1               #[0,2,0,3,1,0,1,3,2,1]
        maxLeft = height[l]                   #maxLeft = 2    , maxRight =1
        maxRight = height[r]

        while l < r:
            if maxLeft <= maxRight: 
                count += maxLeft - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                count += maxRight - height[r]
                r -= 1
                maxRight = max(maxRight, height[r])
        return count
                

