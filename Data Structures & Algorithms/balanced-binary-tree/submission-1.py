# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        def dfs(root):
            if not root:
                return True
            left = height(root.left)
            right = height(root.right)
            print(left, right)
            if ((left - right > 1) or (right - left > 1)):
                return False
            else:
                return (dfs(root.left) and dfs(root.right))
        return dfs(root)
        

        