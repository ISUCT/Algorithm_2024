def bubble(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j][1] < numbers[j+1][1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            if numbers[j][1] == numbers[j+1][1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            if numbers[j][0] > numbers[j+1][0]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

n = int(input())
nums = []
for _ in range(n):
    num1, num2 = map(int, input().split())
    nums.append((num1, num2))

sort = bubble(nums)
for nums in sort:
    print(nums[0], nums[1])

