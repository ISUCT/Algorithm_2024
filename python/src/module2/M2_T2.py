def printArray(arr):
    for i in range(len(arr)):
        print(str(arr[i][0]) + " " + str(arr[i][1]))

def checkIfSortedByElement(arr, elementIndex, reverseMultiplier):
    for i in range(len(arr) - 1):
        if (arr[i][elementIndex] * reverseMultiplier < arr[i + 1][elementIndex] * reverseMultiplier):
            return False
    return True

def makeSortingIterationByElement(arr, elementIndex, reverseMultiplier, endIndex):
    for i in range(endIndex):
        if (arr[i][elementIndex] * reverseMultiplier < arr[i + 1][elementIndex] * reverseMultiplier):
            proc = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = proc

l = int(input())
s = []
for i in range(l):
    inp = input().split()
    s.append(inp) 

iA = []
for i in range(len(s)):
    iA.append([])
    for j in range(len(s[i])):
        iA[i].append(int(s[i][j]))

while (not(checkIfSortedByElement(iA, 0, -1))):
    makeSortingIterationByElement(iA, 0, -1, len(iA) - 1)

for i in range(len(iA) - 1):
    makeSortingIterationByElement(iA, 1, 1, len(iA) - i - 1)

printArray(iA)