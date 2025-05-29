# https://leetcode.com/problems/odd-even-linked-list
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = head
        evens = []
        temp = dummy
        counter = 0
        while current:
            counter += 1
            if counter % 2 == 1:
                temp.next = ListNode(current.val)
                temp = temp.next
            else:
                evens.append(current.val)
            current = current.next
        for item in evens:
            temp.next = ListNode(item)
            temp = temp.next
        return dummy.next
