import sys
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        mindiff = sys.maxint
        res = 0
        for i in xrange(len(numbers)):
        	left = i + 1
        	right = len(numbers) - 1
        	while left < right:
        		sum_ = numbers[i] + numbers[left] + numbers[right]
        		diff = abs(sum_ - target)
        		if diff < mindiff:
        			mindiff = diff
        			res = sum_
        		if sum_ == target:
        			return sum_
        		elif sum_ < target:
        			left += 1
        		else:
        			right -= 1
        return res 

a = Solution()
print a.threeSumClosest([-1,2,1,-4],1)