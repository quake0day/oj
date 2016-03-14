class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            h = {}
            for w in word:
                if w not in h:
                    h[w] = 1
                else:
                    h[w] += 1
            d[word] = h
        print d
        res = []


a = Solution()
print a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])