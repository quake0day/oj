class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        res = num
        while len(str_num) > 1:
            temp_res = 0
            for s in str_num:
                temp_res += int(s)
                
            str_num = str(temp_res)
            res = temp_res
        return res

a = Solution()
print a.addDigits(38)
print a.addDigits(1)
      