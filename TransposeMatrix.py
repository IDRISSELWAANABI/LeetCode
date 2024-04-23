class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M = []
        r_j = []
        for j in range(len(matrix[0])):
            for i in matrix : 
                r_j.append(i[j])
            M.append(r_j)
            r_j = []
        return M


        