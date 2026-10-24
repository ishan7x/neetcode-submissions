from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adjList = []
        for i in range(n):
            adjList.append([])
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        print(adjList)

        currLevel = deque()
        def bfs():
            while(currLevel):
                nodesThisLevel = len(currLevel)
                
                for _ in range(nodesThisLevel):
                    node = currLevel.popleft()
                    seen.add(node)
                    neighbors = adjList[node]
                    for neighbor in neighbors:
                        if neighbor not in seen:
                            currLevel.append(neighbor)
        res = 0
        for i in range(n):
            if i not in seen:
                res+=1
                currLevel.append(i)
                bfs()
        return res
                    




            




        