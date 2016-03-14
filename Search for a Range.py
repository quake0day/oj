class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l+r >> 1
            if nums[mid] == target:
                l = mid
                r = mid
                while l-1 >= 0 and nums[l-1] == target:
                    l -= 1
                while r + 1 < len(nums) and nums[r+1] == target:
                    r += 1

                return [l,r]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1, -1]


a = Solution()
print a.searchRange([1,3], 1)
print a.searchRange([2,2], 2)
print a.searchRange([1,1,2], 1)
print a.searchRange([5, 7, 7, 8, 8, 10], 8)