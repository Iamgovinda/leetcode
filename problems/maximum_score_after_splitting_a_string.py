# https://leetcode.com/problems/maximum-score-after-splitting-a-string
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            max_value = left.count("0") + right.count("1")
            if max_value > result:
                result = max_value
        return result
