N = int(input())
nums = [int(input()) for _ in range(N)]
def bucket_sort(nums, exp, buckets):
    dlina = N
    output = [0] * dlina
    counter = [0] * 10

    for i in range(dlina):
        index_of_1_bucket = nums[i] // exp
        counter[index_of_1_bucket % 10] += 1

    for i in range(1, 10):
        counter[i] += counter[i - 1]

    for i in range(dlina - 1, -1, -1):
        index_of_2_bucket = nums[i] // exp
        output[counter[index_of_2_bucket % 10] - 1] = nums[i]
        counter[index_of_2_bucket % 10] -= 1

    for i in range(dlina):
        nums[i] = output[i]

    print("Bucket status:")
    for i in range(10):
        print(f"Bucket {i}: {', '.join(str(num) for num in buckets[i])}")

def secondary_sort(nums):
    max_num = max(nums)
    exp = 1
    buckets = [[] for _ in range(10)]

    print("Initial array:")
    print(", ".join(str(num) for num in nums))

    while max_num // exp > 0:
        for num in nums:
            buckets[num // exp % 10].append(num)

        bucket_sort(nums, exp, buckets)

        for i in range(10):
            buckets[i] = []

        exp *= 10

    print("Sorted array:")
    print(", ".join(str(num) for num in nums))

secondary_sort(nums)
