class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = float('inf')
        nums = sorted(nums)
        for k in range(len(nums)-1):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] - target < closest:
                    closest = nums[i] + nums[j] + nums[k] - target
                    i += 1
                elif nums[i] + nums[j] + nums[k] - target > closest:
                    j -= 1
        return closest