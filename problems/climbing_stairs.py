# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib_list = []
        a, b = 0, 1
        for _ in range(n):
            fib_list.append(a)
            a, b = b, a + b
        return sum(fib_list) + 1
