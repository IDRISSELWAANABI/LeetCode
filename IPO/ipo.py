class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()       
        max_heap = []
        j = 0
        n = len(projects)
        
        for _ in range(k):
            while j < n and projects[j][0] <= w:
                heapq.heappush(max_heap, -projects[j][1])
                j += 1
            
            if not max_heap:
                break
            w -= heapq.heappop(max_heap)
        
        return w