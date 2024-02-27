file = open("input.txt","r")
len_of_array = int(file.readline())
array = file.readline()
array = array.split()
file.close()
swap_count = 0
file = open("output.txt","w")
for i in range(0,len_of_array-1,1):
    for j in range(0,len_of_array-1,1):
        if int(array[j]) > int(array[j+1]):
            array[j] ,array[j+1] = array[j+1],array[j]
            file.write(" ".join(array)+"\n")
            swap_count +=1
if swap_count == 0:
   file.write("0\n")
file.close()