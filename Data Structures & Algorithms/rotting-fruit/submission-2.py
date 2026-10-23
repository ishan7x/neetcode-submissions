class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        countFresh = 0
        rotCords = []
        for y in range(rows):
            for x in range(columns):
                if (grid[y][x] == 1):
                    countFresh += 1
                elif (grid[y][x] == 2):
                    rotCords.append([x, y])
        # now I have an idea of rotten oranges and fresh oranges
        # I need to get the shortest time in which all are rotten

        minutes = 0

        while((countFresh > 0) and rotCords):
            minutes += 1
            currLevel = len(rotCords)
            print(grid, minutes, countFresh)

            for _ in range(currLevel):
                currCord = rotCords.pop(0)
                right = [currCord[0] + 1, currCord[1]]
                left = [currCord[0] - 1, currCord[1]]
                up = [currCord[0], currCord[1] - 1]
                down = [currCord[0], currCord[1] + 1]

                if (right[0] < columns and grid[right[1]][right[0]] == 1):
                    grid[right[1]][right[0]] = 2
                    countFresh -= 1
                    rotCords.append(right)

                if (left[0] >= 0 and grid[left[1]][left[0]] == 1):
                    grid[left[1]][left[0]] = 2
                    countFresh -= 1
                    rotCords.append(left)

                if (up[1] >= 0 and grid[up[1]][up[0]] == 1):
                    grid[up[1]][up[0]] = 2
                    countFresh -= 1
                    rotCords.append(up)

                if (down[1] < rows and grid[down[1]][down[0]] == 1):
                    grid[down[1]][down[0]] = 2
                    countFresh -= 1
                    rotCords.append(down)
            
        return minutes if (countFresh == 0) else -1            
                





        


        
        
        