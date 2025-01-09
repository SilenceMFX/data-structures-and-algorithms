# Definition for singly-linked list.
from unittest import result


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        result = ListNode(-1)
        prev = result
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        return result.next

    def mergeTwoLists2(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists2(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists2(list1, list2.next)
            return list2
