# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        unique_index = 0
        for index, num in enumerate(nums):
            print(nums[index], nums[unique_index])
            if nums[index] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[index]
        return unique_index + 1
