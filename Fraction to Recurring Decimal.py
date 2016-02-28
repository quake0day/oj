class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        result = []
        if (denominator > 0 and numerator < 0) or (denominator < 0 and numerator > 0):
            result += "-"
        n = int(abs(numerator))
        d = int(abs(denominator))
        r = n % d
        result += str(n/d)
        if r == 0:
            return "".join(result)
        else:
            result += '.'
        hashMap = {}
        while r:
            if r in hashMap:
                result.insert(hashMap[r],"(")
                result += ")"
                break 
            hashMap[r] = len(result)
            r *= 10
            result += str(r/d)
            r = r % d 
        return "".join(result)


a = Solution()
print a.fractionToDecimal(1,3)