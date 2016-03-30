class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[right] + nums[left]
                if sum_ >= target:
                    right -= 1
                else:
                    cnt += right - left 
                    left += 1
        return cnt


a = Solution()
print a.threeSumSmaller([-2, 0, 1, 3], 2)