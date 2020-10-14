def squared(l):
    for i in range(len(l)):
        l[i] *= l[i]
    return l
def merge(a,b):
    c, m, n = [], len(a), len(b)
    i, j = 0, 0
    while i + j < m+n:
        if i == m:
            c.append(b[j])
            j += 1
        elif j == n:
            c.append(a[i])
            i += 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i += 1
        elif a[i] >= b[j]:
            c.append(b[j])
            j += 1
    return c
def sortedSquares(l):
    pos = 0
    if l[0] >= 0:
        a = squared(l)
        return a
    else:
        for i in range(len(l)):
            if l[i] > 0:
                pos = i
                break
        b = squared(l[pos-1::-1])
        c = squared(l[pos:])
    return merge(b,c)
# print(sortedSquares([-4,-3,2,4]))