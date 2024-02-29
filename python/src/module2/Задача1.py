def main():
    znach = int(input())
    if znach == 1:
        m = int(input())
        print(m)
    else:
        k = 0
        m = list(map(int, input().split()))
        for j in range(znach - 1):
            for i in range(znach - 1):
                if m[i] > m[i + 1]:
                    m[i], m[i + 1] = m[i + 1], m[i]
                    k = k + 1
                    if k > 0:
                        print(*m)
        if k == 0:
            print(0)


if __name__ == "__main__":
    main()