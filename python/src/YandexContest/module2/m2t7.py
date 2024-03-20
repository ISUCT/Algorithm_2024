#Поразрядная сортировка

stringCount = int(input())
stringList = []

for i in range(stringCount):
    stringList.append(input())

def radixSort(array, elementLength, abLength):
    process = []
    for i in range(abLength):
        process.append([])
    for i in range(elementLength - 1, -1, -1):
        for j in range(len(array)):
            process[int(array[j][i])].append(array[j])
        count = 0
        for j in range(len(process)):
            for k in range(len(process[j])):
                array[count] = process[j][k]
                count += 1
        printPhase(process, elementLength - i)
        clearProcess(process, abLength)

def printPhase(array, phaseCount):
    print("Phase " + str(phaseCount))
    for i in range(len(array)):
        value = ""
        if len(array[i]) == 0:
            value = "empty"
        else:
            value = ", ".join(array[i])
        print("Bucket " + str(i) + ": " + value)
    print("*" * 10)

def clearProcess(process, abLength):
    for i in range(abLength):
        process[i] = []

print("Initial array:")
print(", ".join(stringList))
print("*" * 10)

radixSort(stringList, len(stringList[0]), 10)

print("Sorted array:")
print(", ".join(stringList))