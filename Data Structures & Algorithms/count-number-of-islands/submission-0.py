class Solution:
    def dfs(self, grid, row, col): 
        if col > 0 and grid[row][col-1] == "1": 
            grid[row][col-1] = 0 
            self.dfs(grid, row, col-1)
        if col < len(grid[0]) - 1 and grid[row][col+1] == '1': 
            grid[row][col+1] = 0 
            self.dfs(grid, row, col+1)
        if row > 0 and grid[row-1][col] == '1': 
            grid[row-1][col] = 0 
            self.dfs(grid, row-1, col)
        if row < len(grid) - 1 and grid[row+1][col] == '1': 
            grid[row+1][col] = 0 
            self.dfs(grid, row+1, col)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                if grid[row][col] == '1': 
                    count += 1
                    grid[row][col] == 0 
                    self.dfs(grid, row, col)
        return count