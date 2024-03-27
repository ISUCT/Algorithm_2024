input = open("input.txt","r")
lenArr = int(input.readline())
arr = input.readline()
arr = arr.split()
input.close()
swap_count = 0
input = open("output.txt","w")
for i in range(0,lenArr-1,1):
    for j in range(0,lenArr-1,1):
        if int(arr[j]) > int(arr[j+1]):
            arr[j] ,arr[j+1] = arr[j+1],arr[j]
            input.write(" ".join(arr)+"\n")
            swap_count +=1
if swap_count == 0:
   input.write("0\n")
input.close()