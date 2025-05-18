N = int(input())
spot = []
for _ in range(N):
    spot.append(list(map(int, input().split())))

spot = sorted(spot, key=lambda x:(x[0], x[1]))

for i in range(N):
    print(spot[i][0], spot[i][1])
    