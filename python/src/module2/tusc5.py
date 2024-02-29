def soedsort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        soedsort(left)
        soedsort(right)
        i = j = l = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[l] = left[i]
                i += 1
            else:
                a[l] = right[j]
                j += 1
            l += 1
        while i < len(left):
            a[l] = left[i]
            i += 1
            l += 1
        while j < len(right):
            a[l] = right[j]
            j += 1
            l += 1

def sortbis(a):
    if len(a) <= 1:
        return a
    else:
        st = a[0]
        men = [x for x in a[1:] if x <= st]
        bol = [x for x in a[1:] if x > st]
        return sortbis(men) + [st] + sortbis(bol)

n = int(input())
num = list(map(int, input().split()))
soedsort(num)
result = []