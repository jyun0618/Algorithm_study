N = int(input())
member = []
for _ in range(N):
    member.append(list(input().split()))

member = sorted(enumerate(member), key=lambda x: (int(x[1][0]), x[0]))
for i in range(N):
    print(member[i][1][0], member[i][1][1])