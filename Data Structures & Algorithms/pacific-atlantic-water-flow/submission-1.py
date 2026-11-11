class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        ROWS = len(heights)
        COLS = len(heights[0])
        
        

        directions = [[-1,0], [1,0], [0,-1], [0,1]]


        pac = []
        for _ in range(ROWS):
            row = []
            for _ in range(COLS):
                row.append(False) 
            pac.append(row)
        
        

        atl = []

        for _ in range(ROWS):
            row = []

            for _ in range(COLS):
                row.append(False)
            
            atl.append(row)

        def bfs(source, ocean): # sourceis where we start, and ocean is the visited tracker
            q = deque(source)

            while q:
                r, c = q.popleft()

                ocean[r][c] = True

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if ( 0<= nr < ROWS and 0 <= nc < COLS and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr,nc))

        pacific = [] # hold all the starting coordinates along the Pacific border.
        atlantic = [] # hold all the starting coordinates along the Atlantic border.
        for c in range(COLS): # used for horizontonal
            pacific.append((0,c))
            atlantic.append((ROWS - 1, c)) # ROWS - 1 nenver moves

        for r in range(ROWS): # used for vertical
            pacific.append((r,0))
            atlantic.append((r, COLS-1)) # COLS -1 never mvoes

        bfs(pacific, pac) # multi source bfs
        bfs(atlantic, atl) # mutli source bfs

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])

        return res

        