# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        d = {}

        def ifbalanced(node):
            if not node:
                d[node] = 0
                return True
            elif not ifbalanced(node.left) or not ifbalanced(node.right):
                return False
            else:
                d[node] = max(d[node.left], d[node.right]) + 1
                return True if abs(d[node.left] - d[node.right]) < 2 else False

        return ifbalanced(root)
