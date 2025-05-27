# https://leetcode.com/problems/maximum-product-of-two-digits
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        while n > 0:
            remainder = n % 10
            nums.append(remainder)
            n = n // 10

        sorted_list = sorted(nums, reverse=True)
        return sorted_list[0] * sorted_list[1]
