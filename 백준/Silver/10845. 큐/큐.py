from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
Q = deque()
for _ in range(N):
    command = input().strip()
    if 'push' in command:
        _, X = command.split()
        Q.append(int(X))
    elif command == 'pop':
        print(Q.popleft() if Q else -1)
    elif command == 'size':
        print(len(Q))
    elif command == 'empty':
        print(0 if Q else 1)
    elif command == 'front':
        print(Q[0] if Q else -1)
    elif command == 'back':
        print(Q[-1] if Q else -1)   