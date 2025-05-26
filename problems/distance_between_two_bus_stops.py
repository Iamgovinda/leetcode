# https://leetcode.com/problems/distance-between-bus-stops/

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            start, destination = destination, start
        clockwise_distance = sum(distance[start:destination])
        anticlockwise_distance = sum(distance[:start]) + sum(distance[destination:])
        return min(clockwise_distance, anticlockwise_distance)