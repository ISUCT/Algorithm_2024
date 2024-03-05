nums = list(map(int, input("Введите числа: ").split()))
def merge_sort(nums):
    n = len(nums)
    if len(nums) == 1:
        return nums
    if len(nums) == 0:
        return nums
    left_half = merge_sort(nums[:len(nums) // 2])
    right_half = merge_sort(nums[len(nums) // 2:])
    i = j = k = 0
#Создаем список zlist, который будет состоять из нулей и по длине равный nums
    zlist = [0] * len(nums)
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            zlist[k] = left_half[i]
            i += 1
        else:
            zlist[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        zlist[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        zlist[k] = right_half[j]
        j += 1
        k += 1
    for i in range(len(nums)):
        nums[i] = zlist[i]
    return nums

merge_sort(nums)
print(nums)
