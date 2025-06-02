# https://leetcode.com/problems/merge-k-sorted-lists/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        items = []
        for head in lists:
            current = head
            while current:
                items.append(current.val)
                current = current.next
        if len(items)==0:
            return None
        items.sort()

        result_head = ListNode(items[0])
        current = result_head

        for val in items[1:]:
            current.next = ListNode(val)  # Create the next node and link it
            current = current.next  # Move to the new node

        return result_head