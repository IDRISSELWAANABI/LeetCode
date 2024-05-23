class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.buildHeap(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heap[0] = num
                self.heapify(heap, 0, k)
        
        return heap[0]
    
    def heapify(self, arr, i, N):    
        smallest = i  
        l = 2 * i + 1  
        r = 2 * i + 2 
        if l < N and arr[l] < arr[smallest]:
            smallest = l 
        if r < N and arr[r] < arr[smallest]:
            smallest = r
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, smallest, N) 
    
    def buildHeap(self, arr):
        N = len(arr)
        startIdx = N // 2 - 1
        for i in range(startIdx, -1, -1):
            self.heapify(arr, i, N)