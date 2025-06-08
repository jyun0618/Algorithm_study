N, m, M, T, R = map(int, input().split())
exercise = 0
time = 0
X = m
if m+T > M:
    print(-1)
else:    
    while exercise < N:
        if X+T <= M:
            X += T
            time += 1
            exercise += 1
        else:
            if X-R < m:
                X = m
            else:
                X -= R
            time += 1
    print(time)