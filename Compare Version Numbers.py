class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        new1 = version1.split(".")
        new2 = version2.split(".")
        score1,score2 = self.getScore(new1, new2)
        print score1, score2
        if score1 > score2:
            return 1
        elif score1 < score2:
            return -1
        return 0
    
    def getScore(self, string1, string2):
        n = len(string1)
        m = len(string2)
        if m != n:
            diff = abs(m - n)
            if m > n:
                while diff > 0:
                    string1.append(0)
                    diff -= 1
            else:
                while diff > 0:
                    string2.append(0)
                    diff -= 1
        score1,score2 = 0,0
        string1 = string1[::-1]
        string2 = string2[::-1]
        for i in xrange(max(n,m)):
            score1 += int(string1[i]) * (10 ** i)
            score2 += int(string2[i]) * (10 ** i)
        return score1, score2

a = Solution()
print a.compareVersion("0.1", "0.0.1")
print a.compareVersion("1", "0")
print a.compareVersion("0.1", "1.0")
