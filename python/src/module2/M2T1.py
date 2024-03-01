def bubble_sort(arr):
    n = len(arr)
    swapped = False

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(' '.join(map(str, arr)))

        if not swapped:
            break

    if not swapped:
        print(0)


N = int(input())
arr = list(map(int, input().split()))

bubble_sort(arr)
