S1, S2, S3 = map(int, input().split())
total = [0] * (S1 * S2 * S3)
for s1 in range(1,S1+1):
    for s2 in range(1,S2+1):
        for s3 in range(1,S3+1):
            total[s1+s2+s3-1] += 1

total_max = max(total)
print(total.index(total_max)+1)