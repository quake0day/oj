

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        intervals.sort(key = lambda x:x.start)
        res = []
        length = len(intervals)
        for i in xrange(length):
        	if res == []:
        		res.append(intervals[i])
        	else:
        		size = len(res)
        		if res[size-1].start <= intervals[i].start <= res[size-1].end:
        			res[size-1].end = max(intervals[i].end, res[size-1].end)
        		else:
        			res.append(intervals[i])
        return res
