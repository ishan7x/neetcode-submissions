# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
""" I think we will first find the depth of right and then print that after which 
it will start print from the left height. 
On the left arm if parent has child then print child otherwise print left"""

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        que = deque()
        que.append(root)

        # res = [root.val]
        res = []
        while que:
            level_size = len(que)

            for i in range(level_size):
                node = que.popleft()

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

                # Last node in this level
                if i == level_size - 1:
                    res.append(node.val)

        return res
            

        

        