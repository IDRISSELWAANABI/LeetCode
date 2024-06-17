class Solution {
public:
    bool judgeSquareSum(int c) {
        for (int prime = 2; prime <= std::sqrt(c); ++prime) {
            if (c % prime == 0) {
                int count = 0;
                while (c % prime == 0) {
                    c /= prime;
                    ++count;
                }
                if (prime % 4 == 3 && count % 2 != 0) {
                    return false;
                }
            }
        }
        return c % 4 != 3;
    }
};
