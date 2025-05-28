# https://leetcode.com/problems/middle-of-the-linked-list

import math
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        current = head
        length = 0
        while current:
            length+=1
            current = current.next
        if length == 1:
            return head
        current = head
        middle_node = int(math.ceil(length/2))
        dummy = ListNode()
        counter = 0
        while current:
            counter+=1
            if counter == middle_node:
                dummy = current.next
            current = current.next
        return dummy