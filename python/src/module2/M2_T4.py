def mergeArrays(firstHalf, secondHalf, startIndex, count):
    resList = []
    curIndex1 = 0
    curIndex2 = 0

    for i in range(len(firstHalf) + len(secondHalf)):
        if (curIndex2 == len(secondHalf) or (curIndex1 < len(firstHalf) and firstHalf[curIndex1] <= secondHalf[curIndex2])):
            resList.append(firstHalf[curIndex1])
            curIndex1 += 1
        else:
            resList.append(secondHalf[curIndex2])
            curIndex2 += 1
            count += len(firstHalf) - curIndex1

    return [resList, count]

def mergeSort(inputArray, startIndex, endIndex):
    if (endIndex - startIndex == 1):
        return [[inputArray[startIndex]], 0]

    middleIndex = int((startIndex + endIndex) / 2)
    ret1 = mergeSort(inputArray, startIndex, middleIndex)
    ret2 = mergeSort(inputArray, middleIndex, endIndex)
    firstHalf = ret1[0]
    secondHalf = ret2[0]
    count = ret1[1] + ret2[1]

    return mergeArrays(firstHalf, secondHalf, startIndex, count)

l = int(input())
s = input().split()
iA = []
for i in range(l):
    iA.append(int(s[i]))

iA = mergeSort(iA, 0, len(iA))

print(iA[1])