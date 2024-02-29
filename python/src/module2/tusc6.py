vid = int(input())
listtov = [int(n) for n in input().split()] 
b = int(input())
list = [int(n) for n in input().split()] 
sche = [0]*(vid+1)
for i in list:
    sche[i]+=1
sche.pop(0)
stopsche = 0
while stopsche < vid:
    if sche[stopsche] > listtov[stopsche]:
        print("yes")
    else:
        print("no")
    stopsche += 1