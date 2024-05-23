class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        int best = nums[0];
        for (int a = 0; a < n; a++) {
            sum = max(sum+nums[a],nums[a]);
            best = max(best,sum);               
        }
        return best ;     
    }
};