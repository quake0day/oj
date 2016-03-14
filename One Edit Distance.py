class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        isTrue = False
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return isTrue
        if abs(m - n) == 1:
            if (m == 1 and n == 0) or (n == 1 and m == 0):
                return True
        l, r = 0, 0
        while l < m and r < n:
            if s[l] == t[r]:
                l += 1
                r += 1
            elif s[l] != t[r] and isTrue == False:
                isTrue = True
                print "HERE"
                if l+1 < m and r + 1 < n and s[l+1] == t[r+1]:
                    l += 1
                    r += 1
                elif l + 1 < m and r < n and s[l+1] == t[r]:
                    l += 1
                elif r + 1 < n and l < m and s[l] == t[r+1]:
                    r += 1
                else:
                    l += 1
                    r += 1
            else:
                return False
                
        return isTrue
a = Solution()
#print a.isOneEditDistance("a", "A")
print a.isOneEditDistance("a", "ac")