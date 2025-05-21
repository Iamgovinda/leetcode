# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i_index, i in enumerate(nums):
            diff = target - i
            try:
                j_index = nums.index(diff)
                if j_index == i_index:
                    j_index = nums.index(diff, j_index + 1)
            except ValueError:
                continue
            return [i_index, j_index]

# test