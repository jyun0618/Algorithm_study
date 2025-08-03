N = int(input())
time = list(map(int, input().split()))

time = sorted(time)
total_time = 0
for i in range(N+1):
    total_time += sum(time[:i])

print(total_time)