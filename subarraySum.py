class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        n = len(nums)
        map_ = {}
        sum_ = 0
        map_[0] = -1
        indexs = []
        for i in xrange(n):
        	sum_ += nums[i]
        	if(sum_ in map_):
        		indexs.append(map_.get(sum_) + 1)
        		indexs.append(i)
        		break
        	map_[sum_] = i
        return indexs

a = Solution()
print a.subarraySum([-3,1,2])
