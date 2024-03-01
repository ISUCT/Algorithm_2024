def merge(listik, listik_1, l, m, h):
    t = l
    i = l
    j = m + 1
    invers = 0
    while i <= m and j <= h:
        if listik[i] <= listik[j]:
            listik_1[t] = listik[i]
            i = i + 1
        else:
            listik_1[t] = listik[j]
            j = j + 1
            invers = invers + (m - i + 1)
        t = t + 1
    while i <= m:
        listik_1[t] = listik[i]
        t = t + 1
        i = i + 1
    for i in range(l, h + 1):
        listik[i] = listik_1[i]
    return invers
 
def merge_sort(listik, listik_1, l, h):
    if h <= l:    
        return 0
    m = l + ((h - l) >> 1)
    invers = 0
    invers = invers + merge_sort(listik, listik_1, l, m)      
    invers = invers + merge_sort(listik, listik_1, m + 1, h)  
    invers = invers + merge(listik, listik_1, l, m, h)     
    return invers

A = int(input())
if A == 1:
    listik = int(input())
    print(0)
else:
    listik = list(map(int, input().split()))
    listik_1 = listik.copy()
    print(merge_sort(listik, listik_1, 0, len(listik) - 1))