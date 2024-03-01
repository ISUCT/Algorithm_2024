def main(C, S):
    count = 0
    for j in range(C - 1):
        for i in range(C - 1):
            if S[i] > S[i + 1]:
                S[i], S[i + 1] = S[i + 1], S[i]
                count += 1
                if count > 0:
                    print(*S)
    if count == 0:
        print(0)


C = int(input())
if C == 1:
    S = int(input())
    print(S)
else:
    S = list(map(int, input().split()))
    main(C, S)