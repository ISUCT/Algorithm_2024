# Utils
def merge(arr1, arr2):
    result = []
    index1 = 0
    index2 = 0

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] < arr2[index2]:
            result.append(arr1[index1])
            index1 += 1
        else:
            result.append(arr2[index2])
            index2 += 1

    while index1 < len(arr1):
        result.append(arr1[index1])
        index1 += 1

    while index2 < len(arr2):
        result.append(arr2[index2])
        index2 += 1

    return result


def merge_sort(arr, print_offset=1):
    if len(arr) <= 1:
        return arr

    split_index = len(arr) // 2

    sorted1 = merge_sort(arr[0:split_index], print_offset)
    sorted2 = merge_sort(arr[split_index:], print_offset + split_index)
    merged = merge(sorted1, sorted2)
    # print(print_offset, print_offset + len(arr) - 1, merged[0], merged[-1])
    return merged


# Input
totals = int(input())
list = list(int(i) for i in input().split(" ") if i.strip() != "")

list = merge_sort(list)
counter = 1
for index in range(len(list) - 1):
    if list[index] != list[index + 1]:
        counter += 1

print(counter)
