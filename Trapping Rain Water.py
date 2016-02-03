class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
        	return 0
        maxL = [0 for _ in xrange(len(height))]
        maxR = [0 for _ in xrange(len(height))]
        max_ = height[0]
        for i in xrange(1, len(height)-1):
        	maxL[i] = max_
        	if max_ < height[i]:
        		max_ = height[i]

        max_ = height[height.size()-1]
        ctrap, ttrap = 0,0
        for i in xrange(len(height)-2, 0, -1):
        	maxR[i] = max_
        	ctrap = min(maxL[i], maxR[i]) - height[i]
        	if ctrap > 0:
        		ttrap += ctrap
        	if max_ < height[i]:
        		max_ = height[i]

        del maxL, maxR
        return ttrap

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 2:
        	return 0

        IBound = [0 for _ in xrange(n)]
        rBound = [0 for _ in xrange(n)]

        h = height[0]

        for i in xrange(n):
        	h = max(h, height[i])
        	IBound[i] = h

        h = height[-1]
        for i in xrange(n-1, -1, -1):
        	h = max(h, height[i])
        	rBound[i] = h

        ret = 0
        for i in xrange(n):
        	res = min(IBound[i], rBound[i]) - height[i]
        	ret += res
        return ret

a = Solution()
print a.trap([0,1,2])