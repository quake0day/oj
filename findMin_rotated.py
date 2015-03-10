class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        min = num[0]
        start, end = 0 , len(num) -1 
        while start + 1 < end:
        	mid = start + (end - start) / 2
        	if num[mid] > num[end]:
        		start = mid + 1
        	elif num[mid] < num[end]:
        		end = mid
        if num[start] > num[end]:
            return num[end]
        else:
            return num[start]
