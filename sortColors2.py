import sys
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        count = 0
        start = 0
        end = len(colors) - 1
        while count < k:
        	minium = sys.maxint
        	maxium = -minium - 1

        	for i in xrange(start, end):
        		minium = min(minium, colors[i])
        		maxium = max(maxium, colors[i])
        	left = start
        	right = end
        	cur = left
        	while cur <= right:
        		if colors[cur] == minium:
        			colors = self.swap(left, cur, colors)
        			cur += 1
        			left += 1
        		elif colors[cur] > minium and colors[cur] < maxium:
        			cur += 1
        		else:
        			colors = self.swap(cur, right, colors)
        			right -= 1
        	count += 2
        	start = left
        	end = right 
        return colors


    def swap(self, left, right, colors):
    	tmp = colors[left]
    	colors[left] = colors[right]
    	colors[right] = tmp
    	return colors


a = Solution()
print a.sortColors2([8,1,10,1,8,8,2,4,9,3,8,1,3,3,6,2,5,1,1,7,1,1,3,9,6,4,6,6,7,2], 10)