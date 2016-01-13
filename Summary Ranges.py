class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        SR = []
        range_start = nums[0]
        range_end = nums[0]
        for i in xrange(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                range_end = nums[i]
            else:
                if range_start != range_end:
                    c = str(range_start)+"->"+str(range_end)
                    SR.append(c)
                else:
                    SR.append(str(range_start))
                range_start = nums[i]
                range_end = nums[i]
        if range_start != range_end:
            c = str(range_start)+"->"+str(range_end)
            SR.append(c)
        else:
            SR.append(str(range_start))
        return SR


a = Solution()
print a.summaryRanges([0,1,2,4,5,7])
