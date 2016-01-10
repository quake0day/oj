class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {}
        hashmap.update({0:-1})
        sum_ = 0
        maxLen = 0
        for i in xrange(len(nums)):
            sum_ += nums[i]
            if sum_ not in hashmap:
                hashmap.update({sum_: i})
            if (sum_ - k) in hashmap:
                index = hashmap.get(sum_ - k)
                maxLen = max(maxLen, i - index)
        print hashmap
        return max(maxLen,0)


a = Solution()
print a.maxSubArrayLen([-2,-1,2,1],3)
