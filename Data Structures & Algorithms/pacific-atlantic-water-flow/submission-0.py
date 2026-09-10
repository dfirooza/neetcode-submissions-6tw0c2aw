class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #given: a rectangular island where each square represents the height 
        #above sea level of the cell 
        #return: all cells that can flow to both the pacific and atlantic oceans 
        #solution: bfs would be better here 
        #start from all of the outside squares, on each step do bfs to find 
        #all adjacent squares to that square that are greater than that value 
        #add them to a list, have one list for pacific and one for atlantic 
        #do either pacific or atlantic first, and on the second run if it's
        #already in the other list then just add its coordinates to final res

        #first get all the blocks adjacent to oceans

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        pac_q = deque()
        atl_q = deque()

        for c in range(cols): 
            pac_q.append((0,c))
            pacific.add((0,c))
        
        for r in range(rows): 
            pac_q.append((r,0))
            pacific.add((r,0))
        
        for c in range(cols): 
            atl_q.append((rows-1, c))
            atlantic.add((rows-1, c))
        
        for r in range(rows): 
            atl_q.append((r, cols - 1))
            atlantic.add((r, cols -1))

        def bfs(queue, visited): 

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue: 
                r, c = queue.popleft()
                for dr, dc in directions: 
                    nr = r + dr
                    nc = c + dc
                
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols 
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                        ): 
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        bfs(pac_q, pacific)
        bfs(atl_q, atlantic)

        return list(pacific & atlantic)

                
                 





        