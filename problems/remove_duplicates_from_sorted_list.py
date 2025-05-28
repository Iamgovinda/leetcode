# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# first solution done by me
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        total = []
        current = head
        while current:
            total.append(current.val)
            current = current.next
        cleaned = list(set(total))
        cleaned.sort()
        dummy = ListNode()
        result = dummy
        for index, item in enumerate(cleaned):
            result.val = item
            if (index + 1 < len(cleaned)):
                result.next = ListNode(cleaned[index + 1])
            else:
                result.next = None
            result = result.next
        return dummy

