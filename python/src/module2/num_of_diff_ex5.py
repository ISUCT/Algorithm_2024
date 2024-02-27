if __name__ == "__main__":
    n = int(input())
    array = input().split()
    for i in range(0,len(array)):
        array[i] = int(array[i])
    print(len(set(array)))
