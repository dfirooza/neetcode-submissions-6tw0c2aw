class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #use bfs here from every land sell
        #if you are on a land cell, run bfs outwards only on neighbors that are also land 
        #until you find one that is a treasure chest
        #once you reach the chest mark it with the number of times bfs has been ran (added a layer)
        #if you reach the edge of the grid without terminating keep the value of that grid with INF

        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        def addRoom(i,j): 
            if (i < 0 or i == rows or j < 0 or j == cols or grid[i][j] == -1 or (i,j) in visited): 
                return
            visited.add((i,j))
            q.append([i,j])

        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 0: 
                    visited.add((i,j))
                    q.append([i,j])

        distance = 0
        while q:
            for i in range(len(q)): 
                i, j = q.popleft()
                grid[i][j] = distance
                addRoom(i+1, j)
                addRoom(i-1, j)
                addRoom(i, j-1)
                addRoom(i,j+1)
            distance += 1
        
    
        
        