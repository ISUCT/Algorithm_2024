N = int(input())

items = []
for _ in range(N):
    id, cost = map(int, input().split())
    items.append((cost, id))

sorted_items = sorted(items, key=lambda x: (-x[0], x[1]))

for cost, id in sorted_items:
    print(id, cost)
