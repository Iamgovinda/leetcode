# https://leetcode.com/problems/valid-word/
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not len(word) >= 3:
            return False
        vowel = False
        consonant = False
        vowels = ["a", "e", "i", "o", "u"]
        for char in word.lower():
            if not char.isalnum():  # Checks if character is not alphanumeric
                return False
            if char.isalpha():
                if char in vowels:
                    vowel = True
                else:
                    consonant = True
        return vowel and consonant
