from collections import deque

def overtakes(p1, p2):
    return 0.5*float(p2[1]**2  - p1[1]**2 + p2[0]**2 - p1[0]**2)/(p2[0] - p1[0])

# assumes consumers is a list of ints and producers a list of int tuples of the form (x,y)
# also assumes the points are ordered by x-axis value and that there aren't two points with the same x coordinate
def getNearest(consumers, producers):
    d = deque()
    for p in producers:
        if len(d) == 0:
            d.append((p, -10**9)) # or min(consumers) - 1
            continue
        cross = overtakes(d[-1][0], p)
        while len(d) > 1 and d[-1][1] > cross:
            d.pop()
            cross = overtakes(d[-1][0], p)
        d.append((p, cross))
    res = []
    idx = 0
    for c in consumers:
        if len(d) > 1 and c >= d[1][1]:
            d.popleft()
        res.append(d[0][0])
    return res