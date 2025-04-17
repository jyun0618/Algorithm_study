N, M = map(int, input().split())
ball = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for m in range(i-1, j):
        if ball[m] != 0:
            ball[m] = 0
        ball[m] = k
print(' '.join(str(x) for x in ball))
