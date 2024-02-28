N = int(input())
items = []
for _ in range(N):
    item_id, cost = map(int, input().split())
    items.append((item_id, cost))


sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))


for item in sorted_items:
    print(item[0], item[1])
