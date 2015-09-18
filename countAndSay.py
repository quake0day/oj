class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        if n <= 0 or n == None:
            return ""

        ret = "1"

        for i in xrange(2,n+1,1):
            temp = ""
            count = 1
            prev = ret[0]
            for j in xrange(1,len(ret),1):
                if ret[j] == prev:
                    count += 1
                else:
                    temp += str(count)
                    temp += prev
                    count = 1
                    prev = ret[j]
            temp += str(count)
            temp += prev
            ret = temp
        return ret




        




a = Solution()
print a.countAndSay(5)

