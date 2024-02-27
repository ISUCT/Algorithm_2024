a = int(input())
lastList = []
for i in range(a):
    mass = list(map(int, input().split()))
    lastList.append(mass)
for i in range(a-1):
    for j in range(a-i-1):
        if (lastList[j][1] < lastList[j+1][1]):
                lastList[j],lastList[j+1] = lastList[j+1],lastList[j]
        elif (lastList[j][1] == lastList[j+1][1]):
            if (lastList[j][0] > lastList[j+1][0]):
                lastList[j],lastList[j+1] = lastList[j+1],lastList[j]
for d in lastList:
    print(str(d[0]) + ' ' + str(d[1]))