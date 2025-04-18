N, M = map(int, input().split())
ball = [n for n in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    ball[i-1], ball[j-1] = ball[j-1], ball[i-1]

print(' '.join(map(str, ball)))