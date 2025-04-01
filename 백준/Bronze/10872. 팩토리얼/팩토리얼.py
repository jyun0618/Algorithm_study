N = int(input())
if N == 0:
    print(1)
else:
    prod = 1
    for i in range(1, N+1):
        prod *= i
    print(prod)