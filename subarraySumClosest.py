import sys
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here

        cur_sum = 0
        sum_ = {}
        n = len(nums)
        for i in xrange(n):
        	cur_sum += nums[i]
        	sum_[i] = cur_sum

        key_sort = sorted(sum_, key=sum_.get)

        min_diff = sys.maxint
        ret = [0] * 2

        for i in xrange(1,len(key_sort)):
        	diff = abs(sum_[key_sort[i]] - sum_[key_sort[i-1]])
        	if diff < min_diff:
        		min_diff = diff
        		ret[0] = min(key_sort[i], key_sort[i-1]) + 1
        		ret[1] = max(key_sort[i], key_sort[i-1])
        return ret


a = Solution()
print a.subarraySumClosest( [-3, 1, 1, -3, 5])
