from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key= lambda interval: interval[0])

        length = len(intervals)

        curNum = 0
        maxNum = 0
        endTimes = []

        for i in range(length):
            curNum += 1
            heappush(endTimes, intervals[i][1])
            print endTimes
            while endTimes and endTimes[0] <= intervals[i][0]:
                heappop(endTimes)
                curNum -= 1

            print endTimes
            maxNum = curNum if curNum > maxNum else maxNum

        return maxNum

a = Solution()
print a.minMeetingRooms([[9,10],[4,9],[4,17]])