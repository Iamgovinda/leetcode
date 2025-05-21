# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # checking first thing first
        if len(s) < 1 or len(s) % 2 != 0:
            return False
        closing_opening_parenthesis_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        # checking basic validation first
        if s[0] in closing_opening_parenthesis_map.keys():
            return False
        if s[-1] in closing_opening_parenthesis_map.values():
            return False
        opening_parentheses_stack = []

        for char in s:
            if char in closing_opening_parenthesis_map.values():
                opening_parentheses_stack.append(char)
                continue
            if char in closing_opening_parenthesis_map.keys():
                if len(opening_parentheses_stack) == 0 or closing_opening_parenthesis_map[char] != \
                        opening_parentheses_stack[-1]:
                    return False
                else:
                    opening_parentheses_stack.pop()
        if len(opening_parentheses_stack) > 0:
            return False
        return True
