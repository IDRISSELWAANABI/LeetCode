class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if not grid:
            return 0

        counter = 0 

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1':
                return
            grid[i][j] = '*'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    counter += 1

        return counter
