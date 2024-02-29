a = int(input())
l = 0
spisok = []

while l < a:
    list = [int(n) for n in input().split()] 
    spisok.append(list)
    l += 1

for r in range(a-1):
    for i in range(a-1):
        if spisok[i][1] < spisok[i+1][1] or (spisok[i][1] == spisok[i+1][1] and spisok[i][0] > spisok[i+1][0]):
            spisok[i], spisok[i+1] = spisok[i+1], spisok[i]

for list in spisok:
    print(' '.join(map(str, list)))