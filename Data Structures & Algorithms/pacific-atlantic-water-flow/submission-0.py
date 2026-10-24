class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        pacific = set()
        atlantic = set()
        result = []

        def dfs(cords: tuple(int, int), ocean: set(tuple(int, int))):
            x, y = cords
            if ((y, x) in ocean):
                return
            ocean.add((y,x))
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if ((0 <= nx < columns) and (0 <= ny < rows) and (heights[ny][nx] >= heights[y][x])):
                    dfs((nx, ny), ocean)
            return
        
        def pacificPopulate():
            for cord in range(columns):
                dfs((cord, 0), pacific)
            for cord in range(rows):
                dfs((0, cord), pacific)

        def atlanticPopulate():
            for cord in range(columns):
                dfs((cord, rows-1), atlantic)
            for cord in range(rows):
                dfs((columns-1, cord), atlantic)
        pacificPopulate()
        atlanticPopulate()

        for cords in pacific:
            if cords in atlantic:
                y,x = cords
                result.append([y,x])
        return result


        


        