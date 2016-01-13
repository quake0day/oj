#class Solution(object):
    #def convert(self, s, numRows):
        #"""
        #:type s: str
        #:type numRows: int
        #:rtype: str
        #"""
        #zigzag_array = []
        #zigzag_s_array = []
        #zigzag_row = numRows - 1
        #if numRows > len(s) or numRows == 1:
            #return s
        #if numRows <= 0:
            #return ""
        #while s != "" :
            #try:
                #part_s = s[0:numRows]
                #zigzag_s = s[numRows]
                #zigzag_array.append(part_s)
                #zigzag_s_array.append(zigzag_s)
                #s = s[numRows+1:]
            #except:
                #break
        #if s != "":
            #zigzag_array.append(s)
        #i = 0
        #res = ""
        #while i <= numRows:
            #try:
                #if i != numRows -2:
                    #for k in zigzag_array:
                        #res += k[i]
                #else:
                    #for k in xrange(len(zigzag_array)):
                        #res += zigzag_array[k][i]
                        #res += zigzag_s_array[k]
                #i += 1
            #except:
                #i += 1
        #return res

class Solution:
    # @return a string

    def convert(self, s, nRows):

        if nRows == 1:

            return s

        result = [''] * nRows

        index = 0
        step = 1

        for i in xrange(len(s)):

            result[index] += s[i]

            # 到达最底下一行，步进-1，递减，开始向上
            if index == nRows - 1:

                step = -1

            # 到达最顶上一行，步进1，递增，开始向下
            if index == 0:

                step = 1

            index += step

        return ''.join(result)
        
a = Solution()
print a.convert("ABCD", 2)

print a.convert("PAYPALISHIRING", 4)
            
             
