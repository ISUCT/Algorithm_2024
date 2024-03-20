#Число инверсий

def mergeSort(a):
    if len(a) <= 1:
        return a,0
    l = a[0:len(a) // 2]
    r = a[len(a) // 2:len(a)]
    l,invl = mergeSort(l)
    r,invr = mergeSort(r)
    merged,inv = merge(l,r)
    inv += invl + invr
    return merged, inv

def merge(a, b):
    i, j, k, count = 0, 0, 0, 0
    c = [0]*(len(a) + len(b))
    while (k < len(c)):
        if (j == len(b) or (i < len(a) and a[i] <= b[j])):
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            count += (len(a) - i)
            j += 1
        k += 1
    return c,count

a = 0
mas = []
def task():
    n = int(input())
    print(mergeSort(list(map(int, input().split())))[1])
task()