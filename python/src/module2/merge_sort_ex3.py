# def merge(left,right,ind_left,ind_right):
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
    # print(ind_left[0]+1,ind_right[-1]+1,c[0],c[-1])
    return c
# def merge_sort(sort_array,sort_ind_arr):
def merge_sort(sort_array,shift = 1):
    if len(sort_array) == 1:
        return sort_array
    else:
        shift_ind = len(sort_array)//2
        left = sort_array[0:shift_ind:1]
        right = sort_array[shift_ind::1]
        # left_ind = sort_ind_arr[0:len(sort_ind_arr)//2:1]
        # right_ind = sort_ind_arr[len(sort_ind_arr)//2:len(sort_ind_arr):1]
        # left = merge_sort(left,left_ind)
        # right = merge_sort(right,right_ind)
        # return merge(left,right,left_ind,right_ind)
        left = merge_sort(left,shift)
        right = merge_sort(right,shift+shift_ind)
        result = merge(left,right)
        print(shift,shift+len(sort_array)-1,result[0],result[-1])
        return result
if __name__ == "__main__":
    file = open("input.txt","r")
    n = int(file.readline())
    array = file.readline().split()
    # ind_arr = []
    # for i in range(0,n):
    #     ind_arr.append(i)
    for i in range(0,n,1):
        array[i] = int(array[i])
    sorted = merge_sort(array)
    for i in range(n):
        print(sorted[i], end = " ")