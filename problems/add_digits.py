# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) == 1:
            return num
        result = num
        while len(str(result)) > 1:
            result = sum([int(n) for n in str(num)])
            num = result
        return result
