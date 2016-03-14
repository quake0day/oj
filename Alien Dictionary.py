import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        proList = set()
        wordset = set()
        for word in words:
            for c in word:
                wordset.add(c)
                
        # for i in xrange(len(words)):
        #     for j in xrange(1, len(words[i])):
        #         if words[i][j-1] != words[i][j]:
        #             proList.add((words[i][j-1], words[i][j]))
        # for i in xrange(1, len(words)):
        #     for j in xrange(min(len(words[i-1]), len(words[i]))):
        #         if words[i-1][j] != words[i][j]:
        #             proList.add((words[i-1][j], words[i][j]))
        
        g = {key:[] for key in wordset}
        #indegree = {key:set() for key in wordset}
        indegree = collections.defaultdict(set)
        # for c in proList:
        #         g[c[0]].append(c[1])
        #         indegree[c[1]] += 1
        #         g[c[1]].append(c[0])
        for i in range(1, len(words)):
            minL = min(len(words[i]), len(words[i-1]))
            for j in range(minL):
                if words[i][j] != words[i-1][j]:
                    indegree[words[i][j]].add(words[i-1][j])
                    g[words[i-1][j]].append(words[i][j])
            
            
        v = [x for x in wordset if x not in indegree]
        q = collections.deque(v)
        final_res = []
        while q:
            node = q.popleft()
            if node in g:
                for c in g[node]:
                    indegree[c].remove(node)
                    #indegree[c] -= 1
                    if len(indegree[c]) == 0:
                        q.append(c)
                        del indegree[c]
            final_res.append(node)
                
        print indegree
        #final_res += sorted([key for key in g.keys() if indegree[key] == 1], key= lambda x: indegree[x], reverse=True)
        return "".join(final_res) if len(indegree) == 0 else ""

a = Solution()
print a.alienOrder(["aac","aabb","aaba"])
print a.alienOrder(["wrt","wrf","er","ett","rftt"])