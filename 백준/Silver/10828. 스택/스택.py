from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
stack = deque()
for _ in range(N):
    command = input().strip()
    if 'push' in command:
        _, X = command.split()
        stack.append(int(X))
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if stack else 1)
    elif command == 'top':
        print(stack[-1] if stack else -1)   