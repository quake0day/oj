class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        L = maxWidth
        res = []
        i = 0
        while i < len(words):
            size = 0; begin = i
            while i < len(words):
                newsize = len(words[i]) if size == 0 else size+len(words[i])+1
                if newsize <= L: size = newsize
                else:
                    break
                i += 1
        print newsize
            



a = Solution()
a.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
            
