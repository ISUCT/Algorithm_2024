def merge_sort_recursive(sequence, start=1):
    if len(sequence) <= 1:
        return sequence, start
    middle = len(sequence) // 2
    left, left_indices = merge_sort_recursive(sequence[:middle], start)
    right, right_indices = merge_sort_recursive(sequence[middle:], start + middle)
    return combine_lists(left, right, [start, start + len(sequence) - 1]), start
def combine_lists(list1, list2, indices_values):
    combined = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    if i < len(list1):
        combined += list1[i:]
    if j < len(list2):
        combined += list2[j:]
    start_idx = indices_values[0]
    end_idx = indices_values[1]
    print(start_idx, end_idx, combined[0], combined[-1])
    return combined

n = int(input())
result, _ = merge_sort_recursive(list(map(int, input().split())))
print(' '.join(map(str, result)))
