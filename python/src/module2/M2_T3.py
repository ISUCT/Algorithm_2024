def mergeArrays(firstHalf, secondHalf, startIndex):
    result = []
    curIndex1 = 0
    curIndex2 = 0

    for i in range(len(firstHalf) + len(secondHalf)):
        if (curIndex2 == len(secondHalf) or (curIndex1 < len(firstHalf) and firstHalf[curIndex1] <= secondHalf[curIndex2])):
            result.append(firstHalf[curIndex1])
            curIndex1 += 1
        else:
            result.append(secondHalf[curIndex2])
            curIndex2 += 1

    print(str(startIndex + 1) + " " + str(startIndex + len(result)) + " " + str(result[0]) + " " + str(result[len(result) - 1]))

    return result

def mergeSort(inputArray, startIndex, endIndex):
    if (endIndex - startIndex == 1):
        return [inputArray[startIndex]]

    middleIndex = int((startIndex + endIndex) / 2)
    firstHalf = mergeSort(inputArray, startIndex, middleIndex)
    secondHalf = mergeSort(inputArray, middleIndex, endIndex)

    return mergeArrays(firstHalf, secondHalf, startIndex)

l = int(input())
s = input().split()
iA = []
for i in range(l):
    iA.append(int(s[i]))

iA = mergeSort(iA, 0, len(iA))

print(" ".join(map(str, iA)))