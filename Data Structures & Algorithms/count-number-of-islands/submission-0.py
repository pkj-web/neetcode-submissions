class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def bfs(row, col):
            q = deque()
            grid[row][col] = "0"
            q.append((row, col))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col

                    if (nc < 0 or nr < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"):
                        continue

                    grid[nr][nc] = "0"
                    q.append((nr, nc))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1

        return islands