class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if ((long long) m * k > bloomDay.size()) {
            return -1;
        }

        int low = 1;
        int high = 1e9;
        while (low < high) {
            int mid = low + (high - low) / 2; 
            if (canMake(bloomDay, m, k, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

private:
    bool canMake(vector<int>& bloomDay, int m, int k, int day) {
        int flowers = 0; 
        int total = 0; 
        for (auto b : bloomDay) {
            if (b <= day) {
                flowers++;
                if (flowers == k) {
                    total++;
                    flowers = 0;
                }
            } else {
                flowers = 0;
            }
            if (total >= m) {
                return true;
            }
        }
        return false; 
    }
};
