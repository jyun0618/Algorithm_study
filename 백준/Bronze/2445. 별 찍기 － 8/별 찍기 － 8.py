N = int(input())
for n in range(1,N+1):
    print('*' * n + ' ' * (N-n) + ' ' * (N-n) + '*' * n)
for n in range(N-1,0,-1):
    print('*' * n + ' ' * (N-n) + ' ' * (N-n) + '*' * n)