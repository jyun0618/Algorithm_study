import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    parts = input().split()
    cmd = parts[0]
    if cmd == 'add':
        if int(parts[1]) not in S:
            S.add(int(parts[1]))
    elif cmd == 'remove':
        if int(parts[1]) in S:
            S.remove(int(parts[1]))
    elif cmd == 'check':
        if int(parts[1]) in S:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if int(parts[1]) in S:
            S.remove(int(parts[1]))
        else:
            S.add(int(parts[1]))
    elif cmd == 'all':
        S = set(range(1,21))
    elif cmd == 'empty':
        S = set()
        
    