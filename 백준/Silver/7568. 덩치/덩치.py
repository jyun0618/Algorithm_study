N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

for i in range(N):
    rank = sum(1 for j in range(N) if people[j][0] > people[i][0] and people[j][1] > people[i][1]) + 1
    print(rank, end=' ')