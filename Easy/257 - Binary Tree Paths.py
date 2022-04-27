# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        path = str(root.val)
        res = []
        self.traverse(root, path, res)
        return res

    def traverse(self, root, path, res):
        if root.left is None and root.right is None:
            res.append(path)
        if root.left is not None:
            self.traverse(root.left, path + "->" + str(root.left.val), res)
        if root.right is not None:
            self.traverse(root.right, path + "->" + str(root.right.val), res)
