n = int(input())
arr = list(map(int, input().split()))
swaps = 0
for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
            print(" ".join(map(str, arr)))
    if swaps == 0:
        print(0)
        break