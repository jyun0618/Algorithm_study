N = int(input())
for n in range(1,N+1):
    print(' ' * (N - n), '*' * (2*n-1), sep='')