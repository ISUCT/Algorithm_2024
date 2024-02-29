def merge(m, m1, low, mid, high):
 
    k = i = low
    j = mid + 1
    inversionCount = 0
    while i <= mid and j <= high:
        if m[i] <= m[j]:
            m1[k] = m[i]
            i = i + 1
        else:
            m1[k] = m[j]
            j = j + 1
            inversionCount += (mid - i + 1)
        k = k + 1
    while i <= mid:
        m1[k] = m[i]
        k = k + 1
        i = i + 1
    for i in range(low, high + 1):
        m[i] = m1[i]
    return inversionCount
 
 
def mergesort(m, m1, low, high):
    if high <= low:    
        return 0
    mid = low + ((high - low) >> 1)
    inversionCount = 0
     
    inversionCount += mergesort(m, m1, low, mid)      
    inversionCount += mergesort(m, m1, mid + 1, high)  
    inversionCount += merge(m, m1, low, mid, high)     
    return inversionCount
 
 
if __name__ == '__main__':
    a = int(input())
    if a == 1:
        m = int(input())
        print(0)
    else:
        m = list(map(int, input().split()))
        m1 = m.copy()
        print(mergesort(m, m1, 0, len(m) - 1))