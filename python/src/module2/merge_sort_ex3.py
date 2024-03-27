def merge(left,right):
    i = 0; j = 0; k = 0; c = [0]*(len(left)+len(right)) 
    while k < len(c):
        if (j == len(right)) or (( i < len(left)) and (left[i] <= right[j])):
            c[k] = left[i]
            i+=1
        else:
            c[k] = right[j]
            j+=1
        k+=1
    return c
def merge_sort(sort_array,shift = 1):
    if len(sort_array) == 1:
        return sort_array
    else:
        shift_ind = len(sort_array)//2
        left = sort_array[0:shift_ind:1]
        right = sort_array[shift_ind::1]
        left = merge_sort(left,shift)
        right = merge_sort(right,shift+shift_ind)
        result = merge(left,right)
        print(shift,shift+len(sort_array)-1,result[0],result[-1])
        return result
if __name__ == "__main__":
    file = open("input.txt","r")
    n = int(file.readline())
    array = file.readline().split()
    for i in range(0,n,1):
        array[i] = int(array[i])
    sorted = merge_sort(array)
    for i in range(n):
        print(sorted[i], end = " ")