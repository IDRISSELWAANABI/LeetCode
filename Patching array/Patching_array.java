class Solution {
    public int minPatches(int[] nums, int n) {
        long  patched = 1 ; 
        int result = 0;
        int i = 0 ; 
        while(patched <= n){
            if(i<nums.length && nums[i] <= patched){
                patched += nums[i];
                i++;
            }else{
                patched+=patched;
                result++;
            }
        }
        return result;
        
    }
}