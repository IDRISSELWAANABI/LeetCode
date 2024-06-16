class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long long patched = 1 ;
        int result = 0;
        int i = 0 ;
        while(patched <= n){
            if(i<nums.size() && nums[i]<=patched){
                patched += nums[i];
                i+=1;
            }else{
                patched += patched; 
                result += 1;
            }
        } 
        return result ;
        
    }
};