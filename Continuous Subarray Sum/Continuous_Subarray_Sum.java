class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        if (k == 0) {
            for (int i = 0; i < nums.length - 1; i++) {
                if (nums[i] == 0 && nums[i + 1] == 0) {
                    return true;
                }
            }
            return false;
        }

        HashMap<Integer, Integer> remainderMap = new HashMap<>();
        remainderMap.put(0, -1); 
        int accumulativeSum = 0;
        
        for (int i = 0; i < nums.length; i++) {
            accumulativeSum += nums[i];
            int remainder = accumulativeSum % k;

            if (remainder < 0) {
                remainder += k;
            }

            if (remainderMap.containsKey(remainder)) {
                if (i - remainderMap.get(remainder) > 1) {
                    return true;
                }
            } else {
                remainderMap.put(remainder, i);
            }
        }
        
        return false;
    }
}
