# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            reverse_value = int(str(x)[::-1])
        else:
            reverse_value = -int(str(abs(x))[::-1])

        if -2 ** 31 <= reverse_value <= 2 ** 31 - 1:
            return reverse_value
        else:
            return 0
