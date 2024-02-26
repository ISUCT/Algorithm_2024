def countSort(arr, maxNum):
    countArr = []
    countArr = countArr + [0] * (maxNum + 1)
    for i in range(len(arr)):
        countArr[arr[i] - 1] += 1
    
    return countArr

def clearProc(proc, alphabetLength):
    for i in range(alphabetLength):
        proc[i] = []

def radixSort(arr, elementLength, alphabetLength):
    proc = []
    result = []

    for i in range(alphabetLength):
        proc.append([])

    for i in range(elementLength - 1, -1, -1):
        for j in range(len(arr)):
            proc[int(arr[j][i])].append(arr[j])

        count = 0
        for j in range(len(proc)):
            for k in range(len(proc[j])):
                arr[count] = proc[j][k]
                count += 1
        printPhase(proc, elementLength - i)
        clearProc(proc, alphabetLength)

def printPhase(arr, phaseCount):
    print("Phase " + str(phaseCount))
    for i in range(len(arr)):
        value = ""
        if(len(arr[i]) == 0):
            value = "empty"
        else:
            value = ", ".join(arr[i])
        print("Bucket " + str(i) + ": " + value)
    print("*" * 10)

stringCount = int(input())
stringList = []

for i in range(stringCount):
    stringList.append(input())

print("Initial array:")
print(", ".join(stringList))
print("*" * 10)

radixSort(stringList, len(stringList[0]), 10)

print("Sorted array:")
print(", ".join(stringList))