class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
    
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in matrix : 
            m = len(i)
            for j in range(m//2):
                i[j],i[m-j-1]=i[m-j-1],i[j]
        