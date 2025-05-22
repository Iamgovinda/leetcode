# https://leetcode.com/problems/find-closest-person/
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        x_to_z = abs(z - x)
        y_to_z = abs(z - y)
        if x_to_z < y_to_z:
            return 1
        elif y_to_z < x_to_z:
            return 2
        else:
            return 0
