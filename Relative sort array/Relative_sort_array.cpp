class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> res;
        vector<int> temp;
        unordered_map<int, int> countMap;
        for (int num : arr1) {
            countMap[num]++;
        }
        for (int num : arr2) {
            while (countMap[num] > 0) {
                res.push_back(num);
                countMap[num]--;
            }
        }
        for (int num : arr1) {
            if (countMap[num] > 0) {
                temp.push_back(num);
                countMap[num]--;
            }
        }
        sort(temp.begin(), temp.end());
        res.insert(res.end(), temp.begin(), temp.end());

        return res;
    }
};