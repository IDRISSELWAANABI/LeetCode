class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total_satisfied = 0
        extra_satisfied = 0
        max_extra_satisfied = 0
        
        for i in range(n):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
            else:
                extra_satisfied += customers[i]
            
            if i >= minutes and grumpy[i - minutes] == 1:
                extra_satisfied -= customers[i - minutes]
            
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        return total_satisfied + max_extra_satisfied
