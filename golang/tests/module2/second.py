size = int(input())
data = []

for _size in range(size):
    iden, val = map(int, input().split())
    data.append((iden, val))

for i in range(size - 1):
    for j in range(size - i - 1):
        if data[j][1] < data[j + 1][1] or (data[j][1] == data[j + 1][1] and data[j][0] > data[j + 1][0]):
            data[j], data[j + 1] = data[j + 1], data[j]

for ite in data:
    print(ite[0], ite[1])