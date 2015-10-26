class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        len_s = len(s)
        isOdd = False
        if len_s % 2 == 0:
        	mid = len_s / 2
        	mid2 = mid + 1
        	isOdd = True
       	else:
       		mid = int(len_s / 2) 

       	if isOdd:
       		s = self.findLongestP(mid, mid2, s, len_s/2)
       	else:
       		s = self.findLongestP_(mid, s, len_s/2)
       	print "HI"
       	return s

    def findLongestP(self, mid, mid2, s, Tround):
    	output = ""
    	isP = True
    	while isP == True:
    		for i in xrange(Tround):
    			if s[mid-i] == s[mid2+i]:
    				output.append(s[mid-i])
    				output.append(s[mid2+i])
    			else:
    				return output
    	
    def findLongestP_(self, mid, s, Tround):
    	output = []
    	output.append(s[mid])
    	isP = True
    	while isP:
    		for i in xrange(1,Tround):
    			if s[mid-i] == s[mid+i]:
    				output.append(s[mid-i])
    				output.append(s[mid+i])
    			else:
    				return output
    	return output



       
a = Solution()
print a.longestPalindrome("abcdzdcab")
