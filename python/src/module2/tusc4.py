def soed2sp(a, b):
    c = []
    i = j = 0
    invconst = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            invconst += len(a) - i
    c += a[i:]
    c += b[j:]
    return c, invconst

def soedsort(s):
    if len(s) <= 1:
        return s, 0
    middle = len(s) // 2
    left, Leftinv = soedsort(s[:middle])
    right, rightinv = soedsort(s[middle:])
    soedlist, inv = soed2sp(left, right)
    return soedlist, Leftinv + rightinv + inv

n = int(input())
result, invconst = soedsort(list(map(int, input().split())))
print(invconst)