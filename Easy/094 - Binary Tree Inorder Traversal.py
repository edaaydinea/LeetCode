# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return [el for el in traverse(root) if el is not None]


def traverse(root):
    if not root: return None
    yield from traverse(root.left)
    yield root.val
    yield from traverse(root.right)
