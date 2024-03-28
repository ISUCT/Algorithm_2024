def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def remove_duplicates(arr):
    arr = quick_sort(arr)
    result = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            result.append(arr[i])
    return result

if __name__ == "__main__":
    n = int(input())
    if n == 1:
        lst = int(input())
        print(lst)
    else:
        lst = list(map(int, input().split()))
    
        lst = remove_duplicates(lst)
        print(len(lst))