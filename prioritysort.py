

def cmp1(c1, c2):
    orderlist = ['o','r','d','e']
    ido = {val:i for i,val in enumerate(orderlist)}
    if c1 in ido.keys() and c2 in ido.keys():
        if ido[c1] > ido[c2]:
            return 1
        elif ido[c1] < ido[c2]:
            return -1
        else:
            return 0
    elif c1 not in ido.keys() and c2 not in ido.keys():
        return c1 > c2
    elif c1 not in ido.keys() and c2 in ido.keys():
        return 1
    else:
        return -1
print sorted("horse", cmp = cmp1)
