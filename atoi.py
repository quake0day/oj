class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):

        # clean the blank ..

        str = str.strip()

        if len(str) == 0:
            return 0

        # write your code here
        ISMinus = self.is_minus(str)
        #print ISMinus

        # if negetive, delete the "-" symbol
        if ISMinus == True:
            str = str[1:]
        
        ISPositive = self.is_positive(str)
        if ISPositive == True:
            str = str[1:]

        ISContainpoint = self.is_containPoint(str)
        #print ISContainpoint

        # If contain dot, then cut it through 
        if ISContainpoint == True:
            str = str.split(".")[0]

        ISValid = self.is_valid(str)

        if not ISValid:
            return 0
        else:
            str = self.take_number(str)
        # judge if it is out of range 
        ISOutofRange = self.is_OutRange(str, ISMinus)

        if ISOutofRange == True:
            if ISMinus:
                return -2147483648
            else:
                return 2147483647
        else:
            final_int = self.convert2Integer(str, ISMinus)
        return final_int



    def is_valid(self, str_):
        if len(self.take_number(str_)) > 0:
            return True
        return False

    def take_number(self, str_):
        valid_symbol = ['+','-']
        valid_str = ['0','1','2','3','4','5','6','7','8','9','.']
        res_str = []
        find_symbol = False
        find_number = False
        for num in str_:
            if find_symbol == False and find_number == False:
                if num in valid_symbol:
                    res_str.append(num)
                    find_symbol = True
                elif num in valid_str:
                    res_str.append(num)
                    find_number = True
            elif find_symbol == True or find_number == True:
                if num in valid_str:
                    res_str.append(num)
                else:
                    return res_str
        return res_str

    def is_containPoint(self, str_):
        if str_.split(".")[0] == str_:
            return False
        else:
            return True


    def is_positive(self, str):
        if str[0] == "+":
            return True
        return False

    def is_minus(self, str):
        if str[0] == "-":
            return True
        elif str[0] == '+':
            return False
        else:
            return False

    def is_OutRange(self, str_, ISMinus):
        if len(str_) > 10:
            return True
        elif len(str_) == 10:
            INT_MAX = "2147483647"
            INT_MIN = "2147483648"
            i = 0
            for num in str_:
                if ISMinus == False:
                    if num > INT_MAX[i]:

                        return True
                else:
                    if num > INT_MIN[i]:
                        return True
                i += 1
            return False
        return False

    def convert2Integer(self, str_, ISMinus):
        j = 0
        res = 0
        try:
            for i in xrange(len(str_)-1,-1,-1):
                res += int(str_[i]) * 10 ** j
                j += 1
            if ISMinus:
                res = res * -1
        except:
            return 0
        return res







a = Solution()
print a.atoi("+1")
print a.atoi("  15+5")
print a.atoi("   +-1111 ")
print a.atoi("")
print a.atoi("       1.0")
print a.atoi("    52lintcode   ")
print a.atoi("1.0")
print a.atoi("-2147483649")
print a.atoi("-2147483648")
print a.atoi("2147483647")
print a.atoi("2147483648")