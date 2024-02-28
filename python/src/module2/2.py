n = int(input())
all_elems = []
for i in range(n):
    nums = list(map(int, input().split()))
    all_elems.append(nums)

for i in range(n-1):
    for j in range(n-1-i):
        if all_elems[j][1] < all_elems[j+1][1]:
            all_elems[j] , all_elems[j+1] = all_elems[j+1], all_elems[j]
        if all_elems[j][1] == all_elems[j+1][1]:
            if all_elems[j][0] > all_elems[j+1][0]:
                all_elems[j] , all_elems[j+1] = all_elems[j+1], all_elems[j]

for i in range(n):
    print(*all_elems[i])