import sys

input = sys.stdin.read()
data = input.split()

N = int(data[0])

integer = list(map(int, data[1:]))

integer.sort()
for i in range(N):
    print(integer[i])