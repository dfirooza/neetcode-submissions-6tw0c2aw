class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0,m): 
            for j in range(0,n): 
                if i == 0 or j == 0: 
                    matrix[i][j] = 1
                else: 
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]"""
        row = [1] * n 
        for i in range(1,m): 
            for j in range(1,n): 
                row[j] += row[j-1]
        return row[n-1]
        