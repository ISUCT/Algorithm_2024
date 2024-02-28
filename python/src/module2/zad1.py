def sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(*arr)
                swapped = True
        if swapped== False:
            print(0)
            break

N = int(input())
arr = list(map(int, input().split()))

sort(arr)
