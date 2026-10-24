class Solution:

    maxArea = 0
    currArea = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        

        def dfs(cords):
            x, y = cords
            grid[y][x] = 0
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x+dx, y+dy
                if (0<=nx<columns and 0<=ny<rows and grid[ny][nx] == 1):
                    self.currArea += 1
                    dfs((nx, ny))
            return
        
        for row in range(rows):
            for column in range(columns):
                self.currArea = 0
                if (grid[row][column] == 1):
                    self.currArea += 1
                    dfs((column, row))
                    self.maxArea = max(self.maxArea, self.currArea)
        
        return self.maxArea

        