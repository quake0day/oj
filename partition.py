class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        result = []
        if s == None or len(s) == 0:
            return result
        path = []
        self.callResult(s, path, 0, result)
        return result

    def callResult(self, s, path, pos, result):
        if (pos == len(s)):
            list_new = list(path)
            result.append(list_new)
            return
        for i in xrange(pos+1, len(s)+1):
            prefix = s[pos:i]
            if(not self.isPalindrome(prefix)):
                continue
            path.append(prefix)
            self.callResult(s, path, i, result)
            path.pop()

            
    def isPalindrome(self, s):
        if str(s)[::-1] == s:
            return True
        return False

a = Solution()
print a.partition("aab")