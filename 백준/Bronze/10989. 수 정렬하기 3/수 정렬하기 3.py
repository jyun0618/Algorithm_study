import sys

arr = [0] * 10001
read = sys.stdin.readline

N = int(read())
for _ in range(N):
    arr[int(read())] += 1

write = sys.stdout.write
for i in range(1, 10001):
    cnt = arr[i]
    if cnt:
        while cnt >= 64:
            write((str(i) + '\n') * 64)
            cnt -= 64
        write((str(i) + '\n') * cnt)
