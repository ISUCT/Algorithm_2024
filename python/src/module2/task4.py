def merge_sort_inversion_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort_inversion_count(arr[:mid])
    right, inv_right = merge_sort_inversion_count(arr[mid:])
    sorted_arr, inversions = merge(left, right)
    return sorted_arr, inversions + inv_left + inv_right

def merge(left, right):
    result = []
    inv = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv += len(left) - i
    result += left[i:]
    result += right[j:]
    return result, inv

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    sorted_nums, inversions = merge_sort_inversion_count(nums)
    print(inversions
