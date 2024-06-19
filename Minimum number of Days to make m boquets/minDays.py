class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        def canMake(bloomDay, m, k, day):
            total = 0
            flowers = 0 
            
            for b in bloomDay :
                if b<=day :
                    flowers += 1
                    if flowers == k :
                        total += 1 
                        flowers = 0
                else : 
                    flowers = 0
                if total >= m :
                    return True 
            return False

        low = 1
        high = max(bloomDay)
        while low < high :
            mid = (low+high)//2
            if canMake(bloomDay, m, k, mid):
                high = mid
            else :
                low = mid+1

        return low 
        