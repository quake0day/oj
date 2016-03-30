class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l, r = 0, 0
        pre = nums[0]
        res = []
        while r < len(nums):
            if nums[r] == pre or pre + 1 == nums[r]:
                pre = nums[r]
            else:
                if nums[l] == pre:
                    res.append(str(nums[l]))
                elif nums[l] != pre:
                    res.append(str(nums[l])+"->"+str(pre))
                pre = nums[r]
                l = r
            r += 1
        if nums[l] == pre:
            res.append(str(nums[l]))
        elif nums[l] != pre:
            res.append(str(nums[l])+"->"+str(pre))   
        return res
        print res 

a = Solution()
print a.summaryRanges([])
print a.summaryRanges([1,2,3,4,6,7,8,10,12,13,14,15,18])