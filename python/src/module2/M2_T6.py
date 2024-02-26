def findMax(arr):
    max = -1
    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]
    return max

def countSort(arr, maxNum):
    countArr = []
    countArr = countArr + [0] * (maxNum + 1)
    for i in range(len(arr)):
        countArr[arr[i] - 1] += 1
    
    return countArr

def processOrders(productCountList, ordersCountList):
    result = []
    for i in range(len(ordersCountList)):
        result.append(checkIfInStock(productCountList, ordersCountList, i))
    return result
        
            
def checkIfInStock(productCountList, ordersCountList, productKind):
    while(ordersCountList[productKind] > 0):
        if(productCountList[productKind] == 0):
            return "yes"
        productCountList[productKind] -= 1
        ordersCountList[productKind] -= 1
    return "no"
    

productKindNum = int(input())
proc = input().split()
productCountList = []


for i in range(productKindNum):
    productCountList.append(int(proc[i]))
orderNum = int(input())

proc = input().split()
orderList = []

for i in range(len(proc)):
    orderList.append(int(proc[i]))

result = processOrders(productCountList, countSort(orderList, findMax(orderList) - 1))
for i in range(len(result)):
    print(result[i])