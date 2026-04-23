class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0 
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == 1: 
                    grid[row][col] = 0 
                    maximum = max(1 + self.dfs(grid, row, col), maximum)
        return maximum
    def dfs(self, grid, row, col): 
        count = 0 
        if col > 0 and grid[row][col-1] == 1: 
            grid[row][col-1] = 0 
            count += 1 + self.dfs(grid, row, col-1)
        if col < len(grid[0]) - 1 and grid[row][col+1] == 1: 
            grid[row][col+1] = 0 
            count += 1 + self.dfs(grid, row, col+1)
        if row > 0 and grid[row-1][col] == 1: 
            grid[row-1][col] = 0 
            count += 1 + self.dfs(grid, row-1, col)
        if row < len(grid) - 1 and grid[row+1][col] == 1: 
            grid[row+1][col] = 0 
            count += 1 + self.dfs(grid, row+1, col)
        return count            