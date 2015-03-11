import sys
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        count1 = {}
        count2 = {}
        for char in target:
        	if char not in count1: 
        		count1[char] = 1
        	else:
        		count1[char] += 1
        for char in target:
        	if char not in count2: 
        		count2[char] = 1
        	else:
        		count2[char] += 1
        count = len(target)
        start = 0
        minSize = sys.maxint
        minStart = 0
        for end in xrange(len(source)):
        	if source[end] in count2 and count2[source[end]] > 0:
        		count1[source[end]] -= 1
        		if count1[source[end]] >= 0:
        			count -= 1
        	if count == 0:
        		while True:
        			if source[start] in count2 and count2[source[start]] > 0:
        				if count1[source[start]] < 0:
        					count1[source[start]] += 1
        				else:
        					break
        			start += 1
        		if minSize > end - start + 1:
        			minSize = end - start + 1
        			minStart = start
        if minSize == sys.maxint:
        	return ''
        else:
        	return source[minStart:minStart+minSize]

