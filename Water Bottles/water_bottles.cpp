class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int res = numBottles ; 
        while(numBottles/numExchange >= 1){
            res = res + numBottles/numExchange;
            numBottles = numBottles/numExchange + numBottles%numExchange;
        }
        return res ; 
        
    }
};