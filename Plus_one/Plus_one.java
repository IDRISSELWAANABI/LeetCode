class Solution {
    public int[] plusOne(int[] digits) {
       int n = digits.length;
       if(digits[n-1]!=9){
           digits[n-1]+=1;
           return digits;
       }else{
           
           int j = n-1;
           while(j>0 && digits[j]==9 ){
               digits[j]=0;
               j--;
                
           }
           if(digits[j]!=9){
               digits[j]+=1;

           }else{
               digits = new int[n+1];
               digits[0]=1;
               
           }
           
           return digits;
           
       }
        
    }
}