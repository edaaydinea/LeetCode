# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            node_deque = deque([(1, root)])
        while node_deque:
            depth, node = node_deque.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))
