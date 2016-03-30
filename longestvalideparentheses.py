def LVP(string):
    c = list(string)
    left, right = 0,0
    sb = []
    for i in xrange(len(c)):
        if c[i] == "(":
            left += 1
            sb.append(c[i])
        elif c[i] == ")" and right < left:
            right += 1
            sb.append(c[i])
    print c

    c = sb
    sb = []
    left, right = 0,0
    for i in xrange(len(c)-1,-1,-1):
        if c[i] == ')':
            right += 1
            sb.append(c[i])
        elif c[i] == "(" and left < right:
            left += 1
            sb.append(c[i])
    print sb[::-1]
LVP("()()))()")
LVP("(())(()")