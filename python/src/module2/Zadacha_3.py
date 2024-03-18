def merg_two_list(left_half, right_half):
    i =0; j = 0; k = 0; arrey = [0]*(len(left_half)+len(right_half))
    while k < len(arrey):
        if (j == len(right_half)) or ((i < len(left_half)) and (left_half[i] <= right_half[j])):
            arrey[k] = left_half[i]
            i = i + 1
        else:
            arrey[k] = right_half[j]
            j = j + 1
        k = k + 1
    return arrey
    
def merg_sort(s, shift = 1):
    if len(s) == 1:
        return s
    else: 
        middle = len(s) // 2
        left = s[0:middle:1]
        right = s[middle::1]
        left = merg_sort(left,shift)
        right = merg_sort(right, shift+middle)
        reult = merg_two_list(left, right)
        print(shift, shift + len(s)-1, reult[0], reult[-1])
        return reult
if __name__ == "__main__":
    a = int(input())
    s = input().split()
    for i in range(0,a,1):
        s[i] = int(s[i])
    s_sort = merg_sort(s)
    for i in range(a):
        print(s_sort[i], end = " ")

