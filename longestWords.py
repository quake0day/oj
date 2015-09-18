class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        longestWord = []
        longestLength = 0
        for item in dictionary:
        	if len(item) > longestLength:
        		longestWord = []
        		longestWord.append(item)
        		longestLength = len(item)
        	elif len(item) == longestLength:
        		longestWord.append(item)
        	else:
        		pass
        return longestWord



a = Solution()

print a.longestWords(["like","love","adss"])
