N, M = map(int, input().split())
bucket = [n for n in range(1,N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    bucket[i-1:j] = bucket[i-1:j][::-1]
print(' '.join(map(str, bucket)))