n = int(input())
counter = 0
items = []

while counter < n:
    item = [int(num) for num in input().split()] 
    items.append(item)
    counter += 1

for _ in range(n-1):
    for i in range(n-1):
        if items[i][1] < items[i+1][1] or (items[i][1] == items[i+1][1] and items[i][0] > items[i+1][0]):
            items[i], items[i+1] = items[i+1], items[i]
        
for item in items:
    print(' '.join(map(str, item)))
