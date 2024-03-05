N = int(input())
nums = list(map(int, input().split()))

def bubbles(nums):
    len_nums = len(nums)
    s = 0
    for i in range(len_nums - 1):
        for j in range(len_nums - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                s += 1
                print(*nums)
    if s == 0:
        print(0)
        
bubbles(nums)

