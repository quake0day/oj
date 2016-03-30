import collections
class Solution:
    # @param {int} n a positive integer
    # @return {int[][]} n x 3 matrix
    def consistentHashing(self, n):
        # Write your code here
        res = [0,359,1]

        q = collections.deque()
        q.append(res)
        k = 1
        while n > 1:
            k += 1
            s, e, idx = q.popleft()
            interval = (e - s) // 2
            new1 = [s, s+interval, idx]
            new2 = [s+interval+1, e, k]
            q.append(new1)
            q.append(new2)
            n -= 1
            q = sorted(list(q), key=lambda x:(x[0]-x[1],x[2]))
            q = collections.deque(q)

        return list(q)


a = Solution()
print a.consistentHashing(6)
            

