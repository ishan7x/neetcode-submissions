class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        seeing = set()
        adjList = []
        for i in range(n):
            adjList.append([])
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        # print(adjList)

        def dfs(node):
            # print("doing dfs: ", node)
            if node in seeing:
                return False

            if node in visited:
                return True

            seeing.add(node)
            neighbors = adjList[node]
            for neighbor in neighbors:
                adjList[neighbor].remove(node)
                if not dfs(neighbor):
                    return False
            seeing.remove(node)
            visited.add(node)
            return True
        
        dfs(0)

        # print(visited)

        return len(visited) == n

        