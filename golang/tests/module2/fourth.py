## Лимит времени на 19 (1.08 секунд)
def merge(arr, mas, low, mid, top):
 
    current = i = low
    forward = mid + 1
    inversionCount = 0
    while i <= mid and forward <= top:
        if arr[i] <= arr[forward]:
            mas[current] = arr[i]
            i += 1
        else:
            mas[current] = arr[forward]
            forward += 1
            inversionCount += (mid - i + 1)
        current += 1
    while i <= mid:
        mas[current] = arr[i]
        current += 1
        i += 1 
    for i in range(low, top + 1):
        arr[i] = mas[i]
    return inversionCount
 
 
def sort(arr, mas, low, top):
    if top <= low:    
        return 0
    mid = low + ((top - low) >> 1)
    inversionCount = 0
    inversionCount += sort(arr, mas, low, mid)      
    inversionCount += sort(arr, mas, mid + 1, top)  
    inversionCount += merge(arr, mas, low, mid, top)     
    return inversionCount
 

if __name__ == '__main__':
    a = int(input())
    if a == 1:
        arr = int(input())
        print(0)
    else:
        arr = list(map(int, input().split()))
        mas = arr.copy()
        print(sort(arr, mas, 0, len(arr) - 1))
