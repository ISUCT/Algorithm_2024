def merge(left,right):
    global inversion_count
    i =0; j = 0; k = 0; c = [0]*(len(left)+len(right))
    while k < len(c):
        if (j == len(right)) or (i < len(left) and left[i] <= right[j]):
            c[k] = left[i]
            i+=1
        else:
            c[k] = right[j]
            j+=1
            inversion_count += len(left)-i
        k+=1
    return c
def merge_sort(what_need_to_sort):
    if len(what_need_to_sort) == 1:
        return what_need_to_sort
    else:
        left_part = what_need_to_sort[0:len(what_need_to_sort)//2:1]
        right_part = what_need_to_sort[len(what_need_to_sort)//2::1]
        left_part = merge_sort(left_part)
        right_part = merge_sort(right_part)
        return merge(left_part,right_part)
if __name__ == "__main__":
    file = open("input.txt","r")
    array_len = int(file.readline())
    array = file.readline().split()
    inversion_count = 0
    file.close()
    for i in range(0,array_len,1):
        array[i] = int(array[i])
    array= merge_sort(array)
    print(inversion_count)
    