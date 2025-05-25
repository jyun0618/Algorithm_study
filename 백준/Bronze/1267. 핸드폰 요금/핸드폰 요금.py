N = int(input())
time = list(map(int, input().split()))
Y = 0
M = 0
for t in time:
    Y += (t // 30 + 1) * 10
    M += (t // 60 + 1) * 15

if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y','M',Y)