class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        dic1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        dic4 = ["", "Thousand", "Million", "Billion"]
        
        
        # 123
        def helperl100(num):
            dic1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            if 1000 > num >= 100:
                res = dic1[num/100] + " Hundred"
                other = helper(num%100)
                if other:
                    return res +" "+ other
                return res
            else:
                return helper(num)
                
        def helper(num):
            dic1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            dic10 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            dic2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            
            if 0 <= num <= 9:
                return dic1[num]
            if 10 <= num <= 19:
                return dic10[num-10]
            if 100 > num >= 20:
                res = dic2[num/10]
                rem = dic1[num%10]
                if not rem:
                    return res
                return res + " " + rem

                
                
        seg = []
        res = []
        while num > 0:
            seg.append(num % 1000)
            num = num // 1000

        for i in range(len(seg)):
            if i > 0 and seg[i] > 0:
                res = [dic4[i]] + res
            res = [helperl100(seg[i])] + res
        return " ".join(res).rstrip()
        

a = Solution()
print a.numberToWords(100)

print a.numberToWords(11901)
print a.numberToWords(20)