# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        pos = dummyHead = ListNode(-1)

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                pos.next = list1
                list1 = list1.next
            else:
                pos.next = list2
                list2 = list2.next

            pos = pos.next

        if list1 is not None:
            pos.next = list1
        if list2 is not None:
            pos.next = list2
        return dummyHead.next
