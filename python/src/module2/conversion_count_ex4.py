def merge(left,right):
    global count
    i =0; j = 0; k = 0; c = [0]*(len(left)+len(right))
    while k < len(c):
        if (j == len(right)) or (i < len(left) and left[i] <= right[j]):
            c[k] = left[i]
            i+=1
        else:
            c[k] = right[j]
            j+=1
            count += len(left)-i
        k+=1
    return c
def merge_sort(sorted):
    if len(sorted) == 1:
        return sorted
    else:
        left_part = sorted[0:len(sorted)//2:1]
        right_part = sorted[len(sorted)//2::1]
        left_part = merge_sort(left_part)
        right_part = merge_sort(right_part)
        return merge(left_part,right_part)
if __name__ == "__main__":
    input = open("input.txt","r")
    arrLen = int(input.readline())
    arr = input.readline().split()
    count = 0
    input.close()
    for i in range(0,arrLen,1):
        arr[i] = int(arr[i])
    arr= merge_sort(arr)
    print(count)
    