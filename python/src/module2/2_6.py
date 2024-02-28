n = int(input())
numberofgoods = list(map(int, input().split()))
k = int(input())
purchases = list(map(int, input().split()))
c = [0] * (n)  # type: list[int]
for i in range(len(purchases)):
    c[purchases[i] - 1] += 1
for i in range(len(numberofgoods)):
    if numberofgoods[i] < c[i]:
        print("Yes")
    else:
        print("No")
