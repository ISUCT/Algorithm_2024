a = int(input())
da = [int(vr) for vr in input().split()] 
const = 0
for l in range(a-1):
    for i in range(a-1):
        if da[i] > da[i+1]:
            const +=1
            da[i], da[i+1] = da[i+1], da[i]
            print(' '.join(map(str, da)))
if const == 0:
    print(0)