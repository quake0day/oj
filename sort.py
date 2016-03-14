A = ['C', 'D', "E", "F", "G"]
B = [3, 0, 4, 1, 2]

def sort(A, B):
    t = zip(A,B)
    t = sorted(t, key=lambda x: x[1])
    A, B = zip(*t)
    return A
print sort(A,B)