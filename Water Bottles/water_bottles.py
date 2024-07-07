class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles // numExchange >= 1 :
            res+=numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return res