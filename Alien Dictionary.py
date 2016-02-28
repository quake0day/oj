import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        less = collections.defaultdict(set)
        greater = collections.defaultdict(set)
        
        for i in xrange(len(words) -1):
            minlen = min(len(words[i]), len(words[i+1]))
            j = 0
            
            while j < minlen and words[i][j] == words[i+1][j]:
                j += 1
            
            if j < minlen:
                less[words[i][j]].add(words[i+1][j])
                greater[words[i+1][j]].add(words[i][j])
        
        charset = set("".join(words))
        print charset
        orderlist = []
        
        deque = collections.deque([x for x in charset if x not in greater])
        print deque
        print greater

        while deque:
            i = deque.popleft()
            if i in less:
                for j in less[i]:
                    greater[j].remove(i)
                    if len(greater[j]) == 0:
                        del greater[j]
                        deque.append(j)
            orderlist.append(i)
        

a = Solution()
print a.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])