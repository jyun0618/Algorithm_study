N = int(input())
seats = list(map(int, input().split()))
want = []
cnt = 0
for n in range(N):
    if seats[n] in want:
        cnt += 1
    else:
        want.append(seats[n])

print(cnt)    