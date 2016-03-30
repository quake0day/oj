class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        m = len(haystack)
        if m == n == 0:
            return 0
        if n == 0:
            return 0
        if m < n:
            return -1
        start = 0
        i = 0
        while i <= m-n:
            if haystack[i] == needle[0]:
                start = i
                j = 0
                while i < m and j < n and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j >= len(needle):
                    return start
                else:
                    i = start + 1
            else:
                i += 1
        return -1


a = Solution()
print a.strStr("mississippi","issip")