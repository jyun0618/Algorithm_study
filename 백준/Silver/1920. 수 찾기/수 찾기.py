N = int(input())
integerN = set(map(int, input().split()))
M = int(input())
integerM = list(map(int, input().split()))

for i in range(M):
    if integerM[i] in integerN:
        print(1)
    else:
        print(0)