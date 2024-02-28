n = int(input())
el = 0
globallist = []

while el < n:
    objectlist = [int(num) for num in input().split()] 
    globallist.append(objectlist)
    el += 1

for raz in range(n-1):
    for i in range(n-1):
        if globallist[i][1] < globallist[i+1][1] or (globallist[i][1] == globallist[i+1][1] and globallist[i][0] > globallist[i+1][0]):
            globallist[i], globallist[i+1] = globallist[i+1], globallist[i]
        
for objectlist in globallist:
    print(' '.join(map(str, objectlist)))