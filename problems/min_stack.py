# https://leetcode.com/problems/min-stack
class MinStack(object):

    def __init__(self):
        self.store = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.store.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.store.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.store[-1] if len(self.store) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.store)
