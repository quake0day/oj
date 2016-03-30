
def match(s, p):
    #invalid input
    if len(p) % 2 != 0:
        return -1

    #reconstruct p
    temp = ''
    i = 0
    while i < len(p):
        #add '*' first
        temp += '*'
        
        #add char pattern
        if p[i+1] == '+':
            temp += p[i] * 2
        else:
            #p[i+1] == '-'
            temp += p[i] * 4
        #iterate to next char 
        i += 2
    p = temp
    print p

    #wildcard matching
    #dp(i,j) the number of ways p[1,i] is matched to s[1,j]
    #if p[i-1] == '*': dp(i,j) = dp(i-1,j) + max(dp(i-1,j-1), dp(i,j-1))
    #                        match 0 times      1 times     >1 times
    #if p[i-1] != '*': dp(i,j) = dp(i-1,j-1) if p[i-1]==s[j-1] else 0

    res = 0

    #i=0
    pre = [0] * (len(s) + 1)
    pre[0] = 1  #i=0, j=0

    now = [0] * (len(s) + 1)
    for i in xrange(1, len(p) + 1):
        #i in [1, len(p)]
        #j = 0
        now[0] = pre[0] if p[i-1] == '*' else 0
        for j in xrange(1, len(s) + 1):
            #j in [1, len(s)]
            if p[i-1] == '*':
                now[j] = pre[j] + max(pre[j-1], now[j-1])
                #match   0 times  1 times    > 1 times
            else:
                now[j] = pre[j-1] if p[i-1] == s[j-1] else 0

            #update result if p is all matched
            if i == len(p):
                res += now[j]
        #iterate to match next i
        pre, now = now, pre
        #print i, pre
    #return reuslt
    return res


print match("waeginsapnaabangpisebbasccepgnccccapisdnfngaabndlrjngeuiogbbegbuoecccc", "a+b+c+c-")
print match("waeginsapnaabangpisebbasepgnccccapisdnfngaabndlrjngeuiogbbegbuoecccc", "a+b+c-")
print match("waeginsapnaabangpisebbasepgnccccapisdnfngaabndlrjngeuiogbbegbuoecccc", "a+c-")
print match("aaaaaa", "a+a-")