class Solution {
    public int minIncrementForUnique(int[] nums) {
        if (nums.length == 0) return 0;
        
        Arrays.sort(nums);
        
        int res = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                int increment = nums[i - 1] - nums[i] + 1;
                res += increment;
                nums[i] += increment;
            }
        }
        
        return res;
    }
}