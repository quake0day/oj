class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        s = s.strip()
        if len(s) == 0 or s == None:
        	return 0

        s = s.split(" ")[-1]
        if len(s) == 0 or s == None:
        	return 0

        return len(s)


a = Solution()
print a.lengthOfLastWord("Hello World ")
print a.lengthOfLastWord("b a ")