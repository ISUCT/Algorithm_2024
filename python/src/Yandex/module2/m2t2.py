#Сортировка пар

n = int(input())
count = 0
mas = []

while count < n:
    objectlist = [int(num) for num in input().split()] 
    mas.append(objectlist)
    count += 1
for j in range(n-1):
    for i in range(n-1):
        if mas[i][1] < mas[i+1][1] or (mas[i][1] == mas[i+1][1] and mas[i][0] > mas[i+1][0]):
            mas[i], mas[i+1] = mas[i+1], mas[i]
        
for objectlist in mas:
    print(' '.join(map(str, objectlist)))