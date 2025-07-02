import sys
input = sys.stdin.readline

n = int(input())
seq = []
cal = []
last_pushed = 0

for i in range(1,n+1):
    N = int(input())
    if not seq or seq[-1] < N:
        for j in range(last_pushed+1, N+1):
            seq.append(j)
            cal.append('+')
        seq.pop()
        cal.append('-')
        last_pushed = N
    elif seq[-1] == N:
        seq.pop()
        cal.append('-')
    else:
        print('NO')
        sys.exit()
        
for c in cal:
    print(c)