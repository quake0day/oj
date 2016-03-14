

def generate(n):
    res = 0
    k = 0
    for i in getValue(n)[::-1]:
        res += 9 ** k * i
        print 9**k*i
        k += 1
    return res 




def getValue(n):
    n = str(n)
    list_ = []
    for i in n:
        if int(i) > 4:
            list_.append(int(i)-1)
        else:
            list_.append(int(i))
    return list_



print generate(1000)