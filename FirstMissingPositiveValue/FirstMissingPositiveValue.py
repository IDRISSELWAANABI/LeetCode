class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        heap = []
        for num in nums:
            if num > 0:
                heapq.heappush(heap, num)
        
        while heap and heap[0] == smallest:
            heapq.heappop(heap)
            smallest += 1
        
        return smallest