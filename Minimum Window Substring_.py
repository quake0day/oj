import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        map_t = collections.Counter(t)
        map_q = {key:0 for key in map_t.keys()}
        minL = len(s)
        start = 0
        l, r = 0, 0
        res = False
        while r < len(s):
            if s[r] in map_t:
                map_q[s[r]] += 1
            while map_q >= map_t and l <= r:
                res = True
                if r-l+1 <= minL:
                    start = max(start, l)
                    minL = min(minL, r-l+1)
                
                if s[l] not in map_q:
                    l += 1
                else:
                    map_q[s[l]] -= 1
                    l += 1
            r += 1
        return s[start:start+minL] if res else ""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == None:
            return ""
        m = collections.Counter(t)
        l = 0
        cnt = 0
        minLen = len(s) + 1
        minStart = 0
        for r in xrange(len(s)):
            if s[r] in m:
                m[s[r]] -= 1
                if m[s[r]] >= 0:
                    cnt += 1
                while cnt == len(t):
                    if r - l + 1 < minLen:
                        minLen = r-l+1
                        minStart = l
                    if s[l] in m:
                        m[s[l]] += 1
                        if m[s[l]] > 0:
                            cnt -= 1
                    l += 1
        if minLen > len(s):
            return ""
        return s[minStart:minStart+minLen]
        
a = Solution()
print a.minWindow("cabwefgewcwaefgcf", "cae")
print a.minWindow("abcabdebac", "cda")

# print a.minWindow("a","b")
# print a.minWindow("ADOBECODEBANC", "ABC")
# print a.minWindow("a", "ab")
# print a.minWindow("ab", "a")
