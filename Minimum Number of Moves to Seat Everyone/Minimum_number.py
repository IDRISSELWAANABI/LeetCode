class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()  
        students.sort()  
        res = 0
        n = len(students)
        for i in range(n):
            res += abs(students[i] - seats[i])  
        return res
