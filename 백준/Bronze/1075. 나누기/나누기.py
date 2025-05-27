N = int(input())
F = int(input())
N = N - N%100
for i in range(100):
    if (N+i)%F == 0:
        print(''.join(['0',str(i)]) if i < 10 else i)
        break