# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummy_head = ListNode(0)
    current = dummy_head

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0  # Value from l1 or 0 if None
        val2 = l2.val if l2 else 0  # Value from l2 or 0 if None

        total = val1 + val2 + carry
        carry, digit = divmod(total, 10)  # Get new digit and carry

        current.next = ListNode(digit)
        current = current.next

        # Move to next nodes
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next
