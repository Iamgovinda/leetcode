# https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for digit in digits:
            number = number * 10 + digit
        number += 1
        result = []

        while number > 0:
            remainder = number % 10
            result.append(remainder)
            number = number // 10
        return result[::-1]
