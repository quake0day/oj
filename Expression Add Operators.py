import collections
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        final_res = []
        if not num or not target:
            return []
        candidate = collections.deque(list(num))
        q = collections.deque([[candidate, []]])
        while q:
            print q
            candidate, ops= q.popleft()
            if len(candidate) >= 2:
                a = candidate.popleft()
                b = candidate.popleft()
                for t in xrange(4):
                    if t == 0:
                        newq = collections.deque([int(a)+int(b)])
                        ops.append('+')
                        newq.extend(candidate)
                        q.append([[newq, ops]])
                    elif t == 1:
                        newq = collections.deque([int(a)-int(b)])
                        ops.append('-')
                        newq.extend(candidate)
                        q.append([[newq, ops]])
                    
                    elif t == 2:
                        newq = collections.deque([int(a)*int(b)])
                        ops.append('*')
                        newq.extend(candidate)
                        q.append([[newq, ops]])
                    else:
                        newq = collections.deque([int(a)*10+int(b)])
                        ops.append('#')
                        newq.extend(candidate)
                        q.append([[newq, ops]])
            elif len(candidate) == 1:
                res, ops = candidate.pop()
                if res == target:
                    final_res.append([[res, ops]])
        return final_res
a = Solution()
print a.addOperators("123", 6)