class Solution {
    public void sortColors(int[] nums) {
        int start = 0 ; 
        int mid = 0;
        int end = nums.length-1 ; 
        while (mid <= end){
            if(nums[mid] == 2 ){
                int temp = 2;
                nums[mid] = nums[end];
                nums[end] = temp;
                end--;
            }else if (nums[mid]==1){
                mid++;
            }else{
                int temp = 0;
                nums[mid] = nums[start];
                nums[start] = temp;
                start++;
                mid++;
            }

        }


        
    }
}