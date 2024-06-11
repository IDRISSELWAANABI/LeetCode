class Solution {
public:
    int heightChecker(std::vector<int>& heights) {
        vector<int> expected = heights;
        sort(expected.begin(), expected.end());
        int res = 0;
        for (size_t i = 0; i < heights.size(); i++) {
            if (heights[i] != expected[i]) {
                res++;
            }
        }

        return res;
    }
};