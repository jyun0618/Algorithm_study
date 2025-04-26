N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
approx = []
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if num[i] + num[j] + num[k] <= M:
                approx.append(num[i] + num[j] + num[k])
print(max(approx))