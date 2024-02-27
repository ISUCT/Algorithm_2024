vid = int(input())
kolvo = list(map(int, input().split()))
zakazi__kolvo = int(input())
zakazi__klientov = list(map(int, input().split()))
z = sorted(set(zakazi__klientov))
b = []
for i in z:
    b.append(zakazi__klientov.count(i))
a = l = 0
while a < len(kolvo) and l < len(b):
    if kolvo[a] < b[l]:
        print('yes')
    else:
        print('no')
    a += 1
    l += 1