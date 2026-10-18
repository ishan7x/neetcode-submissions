# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        def levelOrder(root):
            if not root:
                return
            # left
            levelOrder(root.left)
            # add node 
            self.nodes.append(root.val)
            # right
            levelOrder(root.right)
        levelOrder(root)
        # print(self.nodes[k-1])
        return self.nodes[k-1]



        