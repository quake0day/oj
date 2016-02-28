import bisect
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations, reverse = True)
        print citations
        new = [i+1-citation for i, citation in enumerate(citations)]
        print new
        return bisect.bisect_right([i+1-citation for i,citation in enumerate(citations)], 0)


a = Solution()
print a.hIndex([3, 0, 6, 1, 5])
print a.hIndex([3, 99, 99, 99, 99 ])