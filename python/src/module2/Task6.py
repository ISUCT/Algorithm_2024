Nvid = int(input())
listofTovar = [int(num) for num in input().split()] 
Nzak = int(input())
list = [int(num) for num in input().split()] 
countlist = [0]*(Nvid+1)
for i in list:
    countlist[i]+=1
countlist.pop(0)
stopcounter = 0
while stopcounter < Nvid:
    if countlist[stopcounter] > listofTovar[stopcounter]:
        print("yes")
    else:
        print("no")
    stopcounter += 1
    