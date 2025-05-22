# https://leetcode.com/problems/search-insert-position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            sorted_total = sorted(nums)
            return sorted_total.index(target)
