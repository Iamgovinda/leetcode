# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # current1
        current1 = l1
        value_list1 = []
        while current1:
            value_list1.append(current1.val)
            current1 = current1.next

        # current2
        current2 = l2
        value_list2 = []
        while current2:
            value_list2.append(current2.val)
            current2 = current2.next
        result = [ListNode(val=int(d), next=None) for d in
                  str(int(''.join(map(str, value_list1[::-1]))) + int(''.join(map(str, value_list2[::-1]))))[::-1]]
        for index, item in enumerate(result):
            try:
                item.next = result[index + 1]
            except IndexError as e:
                item.next = None
        return result[0]
