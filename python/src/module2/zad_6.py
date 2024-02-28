n = int(input())


stock_counts = list(map(int, input().split()))


k = int(input())


orders = list(map(int, input().split()))


order_counts = [0] * n


for order in orders:
    order_counts[order - 1] += 1


for i in range(n):
    if stock_counts[i] < order_counts[i]:
        print("yes")
    else:
        print("no")
