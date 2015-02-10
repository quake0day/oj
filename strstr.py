class Solution:
    def strStr(self, source, target):
        if target in source:
            return 1
        return -1


a = Solution()
print a.strStr("source","target")
print a.strStr("abcdabcdefg","bcd")