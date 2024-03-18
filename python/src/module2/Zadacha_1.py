if __name__ =="__main__":
    death = input()
    arrey = input()
    arrey = arrey.split()
    count = 0
    for i in range(0, len(arrey)-1):
        for j in range(0, len(arrey)-1):
            if int(arrey[j]) > int(arrey[j+1]):
                arrey[j], arrey[j + 1] = arrey[j + 1], arrey[j]
                print(" ".join(arrey))
                count += 1
    if count == 0:
        print(0)