a = ["was", "war"]
def k(a):
    res = []
    for c in a:
        res.append(c)
    return res

print set(map(k, [t for t in a]))