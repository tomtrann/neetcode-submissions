class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 0;
        int cur = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                cur++;
            }
            if (nums[i] == 0){
                if (cur >= max){
                max = cur;
                }
                cur = 0;
            }
        }
        
        max = std::max(max, cur);
        return max;
    }
};