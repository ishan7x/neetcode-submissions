# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodesHelper(self, root, maxVal):
        if not root:
            return 0
        if (root.val < maxVal):
            return (self.goodNodesHelper(root.left, maxVal) + self.goodNodesHelper(root.right, maxVal))
        else:
            maxVal = root.val
            return 1 + (self.goodNodesHelper(root.left, maxVal) + self.goodNodesHelper(root.right, maxVal))

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, root.val - 1)
        
        