# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        prev = slow = fast = head

        new_list = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            prev.next = new_list
            new_list = prev

        if fast:
            slow = slow.next

        while new_list and slow:
            if new_list.val != slow.val:
                return False
            new_list = new_list.next
            slow = slow.next
        return True