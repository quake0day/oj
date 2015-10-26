class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        a = len(digits) - 1
        f = 0.0
        for item in digits:
            f += 10 ** int(a) * int(item)
            a -= 1
        f = int(f)
        f += 1
        res = []
        while f > 0:
            k = f % 10 
            res.append(k)
            f = f / 10
        res = res[::-1]
        return res


a = Solution()
print a.plusOne([9,9,9])