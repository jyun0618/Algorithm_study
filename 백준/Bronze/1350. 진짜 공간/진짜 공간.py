N = int(input())
file = list(map(int, input().split()))
cluster = int(input())

disc = 0
for i in range(N):
    if file[i] == 0:
        continue
    else:
        if file[i] % cluster == 0:
            disc += cluster * (file[i] // cluster)
        else:
            disc += cluster * (file[i] // cluster + 1)

print(disc)