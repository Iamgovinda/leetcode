# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pass


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        guessed_number = (start + end) // 2
        result = guess(guessed_number)
        while result != 0:
            if result == -1:
                end = guessed_number - 1
                guessed_number = (start + end) // 2
                result = guess(guessed_number)
            elif result == 1:
                start = guessed_number + 1
                guessed_number = (start + end) // 2
                result = guess(guessed_number)
        return guessed_number
