def part(arr, startIndex, endIndex):
    firstIndex = startIndex
    secondIndex = endIndex - 1
    anchorIndex = int((startIndex + endIndex - 1) / 2)
    anchorElement = arr[anchorIndex]

    while(firstIndex <= secondIndex):
        while(arr[firstIndex] < anchorElement):
            firstIndex += 1

        while(arr[secondIndex] > anchorElement):
            secondIndex -= 1

        if(firstIndex >= secondIndex):
            break

        arr[firstIndex], arr[secondIndex] = arr[secondIndex], arr[firstIndex]

        firstIndex += 1
        secondIndex -= 1

    return secondIndex + 1
    

def quickSort(arr, startIndex, endIndex):

    if(endIndex - startIndex <= 1):
        return

    anchorIndex = part(arr, startIndex, endIndex)

    quickSort(arr, startIndex, anchorIndex)
    quickSort(arr, anchorIndex, endIndex)

def countDifferentNumbers(arr):
    res = len(arr)

    for i in range(len(arr) - 1):
        if(arr[i] == arr[i + 1]):
            res -= 1
   
    return res

l = int(input())
s = input().split()
iA = []
for i in range(l):
    iA.append(int(s[i]))

quickSort(iA, 0, len(iA))

print(countDifferentNumbers(iA))