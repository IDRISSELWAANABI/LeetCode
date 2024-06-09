class Solution {
public:
    bool checkSubarraySum(std::vector<int>& nums, int k) {
        if (k == 0) {
            for (int i = 0; i < nums.size() - 1; ++i) {
                if (nums[i] == 0 && nums[i + 1] == 0) {
                    return true;
                }
            }
            return false;
        }

        std::unordered_map<int, int> remainderMap;
        remainderMap[0] = -1; 
        int accumulativeSum = 0;
        
        for (int i = 0; i < nums.size(); ++i) {
            accumulativeSum += nums[i];
            int remainder = accumulativeSum % k;

            if (remainder < 0) {
                remainder += k;
            }

            if (remainderMap.find(remainder) != remainderMap.end()) {
                if (i - remainderMap[remainder] > 1) {
                    return true;
                }
            } else {
                remainderMap[remainder] = i;
            }
        }
        
        return false;
    }
};
