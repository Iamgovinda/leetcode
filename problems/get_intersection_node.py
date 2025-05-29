# https://leetcode.com/problems/intersection-of-two-linked-lists
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodesA = set()
        nodesB = set()
        while headA or headB:
            if headA:
                if headA in nodesB:
                    return headA
                nodesA.add(headA)
                headA = headA.next
            if headB:
                if headB in nodesA:
                    return headB
                nodesB.add(headB)
                headB = headB.next


