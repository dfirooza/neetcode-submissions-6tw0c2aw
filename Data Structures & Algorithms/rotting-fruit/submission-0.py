class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #this is a bfs problem 
        #have a list of all the good fruits initially 
        #do simultaneous bfs from each good fruit each minute, but only going out 1 no recursion
        #each time a good fruit goes bad pop it from the list 
        #base case is when the list is empty

        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # seed queue with all initially rotten oranges, count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def addOrange(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1:
                return
            nonlocal fresh
            grid[r][c] = 2
            fresh -= 1
            q.append((r, c))

        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addOrange(r + 1, c)
                addOrange(r - 1, c)
                addOrange(r, c + 1)
                addOrange(r, c - 1)
            minutes += 1

        return minutes if fresh == 0 else -1