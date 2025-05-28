# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        length_of_list = 0
        current = head

        while current:
            length_of_list += 1
            current = current.next
        if length_of_list == 1 and n == 1:
            return None
        if length_of_list < n:
            return head
        if n == 0:
            return head

        current = head
        front_index = length_of_list - n
        if front_index == 0:
            return head.next
        counter = 0
        while current.next:
            counter += 1
            if counter == front_index:
                current.next = current.next.next
            else:
                current = current.next
        return head
