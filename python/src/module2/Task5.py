def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        Left = arr[:mid]
        Right = arr[mid:]
        merge_sort(Left)
        merge_sort(Right)
        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

n = int(input())
numbers = list(map(int, input().split()))
merge_sort(numbers)
resultWithoutOrdinary = []
for el in range(n-1):
    if numbers[el] != numbers[el+1]:
        resultWithoutOrdinary.append(numbers[el])
resultWithoutOrdinary.append(numbers[-1])
print(len(resultWithoutOrdinary))