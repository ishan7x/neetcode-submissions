"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = []
        maps = {}
        # idea is to do a depth first search and store it in a map. Then recreate the graph from the map
        if not node:
            return None
        
        def dfs(node):
            if node in maps:
                return maps[node]

            neighbors = node.neighbors
            newNode = Node(node.val)
            maps[node] = newNode
            for i in neighbors:
                newNode.neighbors.append(dfs(i))
            return newNode
        return dfs(node)

        
        