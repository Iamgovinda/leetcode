# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle in haystack:
            return -1

        return haystack.find(needle)
