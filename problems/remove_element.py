# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while (i < len(nums)):
            if nums[i] == val:
                del nums[i]
                i = i - 1
            i = i + 1
