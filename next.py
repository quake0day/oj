class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        target = -1
        for i in xrange(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                target = i-1
                break
        if target != -1:
            for i in xrange(len(nums)-1, -1,-1):
                if nums[i] > nums[target]:
                    nums[i], nums[target] = nums[target], nums[i]
                    break
            idx = min(i, target)
            nums[idx+1:] = sorted(nums[idx+1:])
        else:
            nums = sorted(nums)
        print nums
                

a = Solution()
print a.nextPermutation([3,2,1])