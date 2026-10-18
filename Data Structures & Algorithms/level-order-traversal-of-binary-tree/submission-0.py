# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        if (not root):
            return []
        
        que.append(root)

        res = []
        while que:
            currLvl = []
            for _ in range(len(que)):
                curr = que.popleft()
                if (curr.left):
                    que.append(curr.left)
                if (curr.right):
                    que.append(curr.right)
                currLvl.append(curr.val)
            res.append(currLvl)
        
        return res


