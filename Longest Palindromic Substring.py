class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        def getlongestpalidrome(self, s, l, r):
        	while l >= 0 and r < len(s) and s[l] == s[r]:
        		l -= 1; r += 1
        	return s[l+1 : r]


        def longestPalindrome(self, s):
        	palindrome = ''
        	for i in xrange(len(s)):
        		len1 = len(self.getlongestpalidrome(s, i , i))
        		if len1 > len(palindrome): palindrome = self.getlongestpalidrome(s, i , i)
        		len2 = len(self.getlongestpalidrome(s, i, i+1))
        		if len2 > len(palindrome): palindrome = self.getlongestpalidrome(s, i, i+1)

        	return palindrome