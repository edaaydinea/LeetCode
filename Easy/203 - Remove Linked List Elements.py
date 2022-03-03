# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(-1, head)
        prev = node
        while head is not None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return node.next
