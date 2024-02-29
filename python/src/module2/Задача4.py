def merge(m, M, low, middle, high):
 
    k = low
    i = low
    j = middle + 1
    inversions = 0
    while i <= middle and j <= high:
        if m[i] <= m[j]:
            M[k] = m[i]
            i += 1
        else:
            M[k] = m[j]
            j += 1
            inversions += (middle - i + 1)
        k += 1
    while i <= middle:
        M[k] = m[i]
        k += 1
        i += 1
    for i in range(low, high + 1):
        m[i] = M[i]
    return inversions
 
 
def mergesort(m, M, low, high):
    if high <= low:    
        return 0
    middle = low + ((high - low) >> 1)
    inversions = 0
     
    inversions += mergesort(m, M, low, middle)      
    inversions += mergesort(m, M, middle + 1, high)  
    inversions += merge(m, M, low, middle, high)     
    return inversions
 
 
if __name__ == '__main__':
    a = int(input())
    if a == 1:
        m = int(input())
        print(0)
    else:
        m = list(map(int, input().split()))
        M = m.copy()
        print(mergesort(m, M, 0, len(m) - 1))