class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
    	min = num[0]
    	start,end = 0, len(num) - 1
    	while start < end:
    		mid = start + (end - start) / 2
    		if num[mid] > num[end]:
    			start = mid + 1
    		elif num[mid] < num[end]:
    			end = mid
    		else:
    			end -= 1
    	return num[start]