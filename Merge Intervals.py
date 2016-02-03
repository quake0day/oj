# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []: return []
        intervals.sort(key = lambda x: x.start)
        res = []
        prev = Start = End = None
        for curr in intervals:
        	if prev:
        		if curr.start <= End:
        			End = max(End, curr.end)
        		else:
        			res.append([Start, End])
        			Start = curr.start
        			End = curr.end

        	else:
        		Start = curr.start
        		End = curr.end
        	prev = curr