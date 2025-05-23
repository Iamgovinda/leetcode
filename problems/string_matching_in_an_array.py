# https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        total_sub_words = []
        for w in words:
            for word in words:
                if w != word and w in word:
                    total_sub_words.append(w)
                    break
        return total_sub_words
