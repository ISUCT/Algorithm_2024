file = open("input.txt","r")
len_of_array = int(file.readline())
array_of_numbers = []
array_of_prices = []
for i in range (0,len_of_array,1):
    string = file.readline().split()
    string[0] = int(string[0])
    array_of_numbers.append(string[0])
    string[-1] = int(string[-1])
    array_of_prices.append(string[-1])
file.close()
file = open("output.txt","w")
for i in range(0,len_of_array-1,1):
    for j in range(0,len_of_array-1,1):
        if int(array_of_prices[j]) == array_of_prices[j+1]:
            if int(array_of_numbers[j]) < array_of_numbers[j+1]:
                array_of_prices[j] ,array_of_prices[j+1] = array_of_prices[j+1],array_of_prices[j]
                array_of_numbers[j] ,array_of_numbers[j+1] = array_of_numbers[j+1],array_of_numbers[j]
        else:
            if int(array_of_prices[j]) > array_of_prices[j+1]:
                array_of_prices[j] ,array_of_prices[j+1] = array_of_prices[j+1],array_of_prices[j]
                array_of_numbers[j] ,array_of_numbers[j+1] = array_of_numbers[j+1],array_of_numbers[j]
for i in range(len_of_array-1,-1,-1):
    file.write(str(array_of_numbers[i])+" "+str(array_of_prices[i])+"\n")
file.close()