class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        room_axis = []
        max_ = 0
        for i in xrange(len(intervals)):
            room_axis.append((intervals[i][0],1))
            room_axis.append((intervals[i][1],-1))
        room_axis = sorted(room_axis, key=lambda x: (x[0], x[1]))
        print room_axis
        needRoom = 0
        print room_axis
        for event in room_axis:

            needRoom += event[1]
            max_ = max(max_, needRoom)
        return max_

a = Solution()
print a.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
print a.minMeetingRooms([[13,15],[1,13]])