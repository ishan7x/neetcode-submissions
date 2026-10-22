class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x,y):
            # has to change every neighbour 1 to 0 check all directions x-1, y : x+1, y: x, y-1 : x, y+1][x+1]
            # print("doing dfs for x, y", x, y)
            if (x - 1 >= 0 and grid[y][x-1] == "1"):
                # fix left
                grid[y][x-1] = "0"
                dfs(x-1, y)
            if (x + 1 < n and grid[y][x+1] == "1"):
                # fix right
                grid[y][x+1] = "0"
                dfs(x+1, y)
            if (y - 1 >= 0 and grid[y-1][x] == "1"):
                # fix up
                grid[y-1][x] = "0"
                dfs(x, y-1)
            if (y+1 < m and grid[y+1][x] == "1"):
                # down
                grid[y+1][x] = "0"
                dfs(x, y+1)
            return

        for y in range(m):
            for x in range(n):
                # print(grid[y][x])
                # print("res is ", res)
                if (grid[y][x] == "1"):
                    dfs(x, y)
                    res+=1
        return res


        