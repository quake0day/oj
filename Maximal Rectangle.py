class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []: return 0
        a = [0 for i in xrange(len(matrix[0]))]; maxArea = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                a[j] = a[j] + 1 if matrix[i][j] == '1' else 0

            maxArea = max(maxArea, self.largestRectangleArea(a))
        return maxArea
        
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        maxArea = 0
        h = heights + [0]
        h_length = len(h)
        while i < h_length:
            if (not stack) or h[stack[-1]] < h[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, h[t] * (i if not stack else i - stack[-1] - 1))
        return maxArea