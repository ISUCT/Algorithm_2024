def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


N = int(input())


numbers = list(map(int, input().split()))


sorted_numbers = quick_sort(numbers)


unique_count = 1

for i in range(1, N):
    if sorted_numbers[i] != sorted_numbers[i - 1]:
        unique_count += 1


print(unique_count)
