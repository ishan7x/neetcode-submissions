# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # I will go through it with in BFS and check each node keeping track of max and min 
        stack = deque()
        if not root:
            return True
        stack.append([root, float('-inf'), float('inf')])
        while stack:
            node = stack.popleft()
            print(stack[0][0].val) if stack else print("empty")
            if (node[0].left):
                if (node[1] < node[0].left.val < node[0].val):
                    stack.append([node[0].left, node[1], node[0].val])
                    print("left")
                else:
                    return False
            if (node[0].right):
                if (node[2] > node[0].right.val > node[0].val):
                    stack.append([node[0].right, node[0].val, node[2]])
                    print("right")
                else:
                    return False
        return True

        