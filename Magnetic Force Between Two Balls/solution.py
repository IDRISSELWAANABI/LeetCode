class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = (position[-1] - position[0]) // (m - 1)
        res = 1
        while left <= right : 
            mid = left + (right-left)//2
            if self.feasible(position, mid, m):
                res = mid 
                left = mid+1
            else : 
                right = mid-1
        return res 

    def feasible(self , arr , dist , balls) :
        number_balls = 1
        last_added = arr[0]
        for i in range(1, len(arr)):
            if arr[i]-last_added >= dist : 
                number_balls+=1
                last_added = arr[i]
            if number_balls >= balls : 
                return True 
        return False 

        



