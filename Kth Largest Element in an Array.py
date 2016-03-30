class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        start = 0
        
        for i in xrange(1, len(nums)):
            if nums[i] > pivot:
                start += 1
                nums[i], nums[start] = nums[start], nums[i]
            print pivot, nums
        nums[start], nums[0] = nums[0], nums[start]
        print start + 1
        print nums
        
        if start + 1 == k:
            return pivot
        elif start + 1 > k:
            return self.findKthLargest(nums[:start], k)
        else:
            return self.findKthLargest(nums[start+1:], k-start-1)
            
        

a = Solution()
print a.findKthLargest([3,2,1,5,6,4], 2)