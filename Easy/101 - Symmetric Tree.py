# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root, root)]

        while stack:
            node1, node2 = stack.pop()
            if node1 is None and node2 is None:
                pass
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
        return True
