class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        self.pair = []
        def helper(i, words):
            word = words[i]
            for j in xrange(len(words)):
                if j != i:
                    c = words[j][::-1]
                    if c[:len(word)] == word and c[len(word):] == c[len(word):][::-1]:
                        self.pair.append([i, j])
        
        for i in xrange(len(words)):
            helper(i, words)
        return self.pair


a = Solution()
print a.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
print a.palindromePairs(["bat", "tab", "cat"])