def soed2sp(a, b, Ind):
    const = []
    i = j = 0
    while i <len(a) and j < len(b):
        if a[i] < b[j]:
            const.append(a[i])
            i+=1
        else:
            const.append(b[j])
            j+=1
    if i<len(a):
        const += a[i:]
    if j<len(b):
        const += b[j:]
    stind = Ind[0]
    endind = Ind[1]
    print(stind, endind, const[0], const[-1])
    return const

def soedsort(s, start=1):
    if len(s) <= 1:
        return s, start
    middle = len(s)//2
    left, left_Ind = soedsort(s[:middle], start)
    right, right_Ind = soedsort(s[middle:], start + middle)
    return soed2sp(left, right, [start, start + len(s) - 1]), start

n = int(input())
result, _ = soedsort(list(map(int, input().split())))
print(' '.join(map(str, result)))