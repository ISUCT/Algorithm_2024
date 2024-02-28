def printArray(arr):
    for i in range (len(arr)):
        if (i == len(arr) - 1):
            print(str(arr[i]))
            return
        print(str(arr[i]) + " ", end="")

def checkIfSorted(arr):
    for i in range(len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            return False
    return True

def makeSortingIteration(arr, endIndex):
    for i in range(endIndex):
        if (arr[i] > arr[i + 1]):
            proc = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = proc
            printArray(arr)

l = int(input())
s = input().split()
iA = []
for i in range(len(s)):
    iA.append(int(s[i]))

if (checkIfSorted(iA)):
    print(0)
else:
    for i in range(len(iA)):
        makeSortingIteration(iA, len(iA) - i - 1)