import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
Ns = list(map(int, data[1:N+1]))
M = int(data[N+1])
Ms = list(map(int, data[N+2:]))

counter = {}
for n in Ns:
    counter[n] = counter.get(n, 0) + 1
    
print(' '.join(str(counter.get(m, 0)) for m in Ms))