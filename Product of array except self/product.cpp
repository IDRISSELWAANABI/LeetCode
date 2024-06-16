class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        int left_product = 1;
        for (int i = 0; i < n; ++i) {
            res[i] = left_product;
            left_product *= nums[i];
        }
        int right_product = 1;
        for (int i = n - 1; i >= 0; --i) {
            res[i] *= right_product;
            right_product *= nums[i];
        }

        return res;
    }
};
