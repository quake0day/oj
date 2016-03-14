import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for i in xrange(len(nums)):
            heapq.heappush(h, -nums[i])
        for _ in xrange(k):
            res = heapq.heappop(h)
        return -res


a = Solution()
print a.findKthLargest([3,2,1,5,6,4], 2)