


def reverse(s):
    vow = ['a', 'e', 'i', 'o', 'u']
    if len(s) <= 1:
        return s 
    i, j = 0, len(s) - 1
    tmp = list(s)
    while i < j:
        if tmp[i] not in vow:
            i += 1
        elif tmp[j] not in vow:
            j -= 1
        else:
            tmp[i], tmp[j] = tmp[j], tmp[i]
            i +=1
            j -= 1
    return "".join(tmp)


print reverse('united states')
print reverse('yyyyyyyyyyy')