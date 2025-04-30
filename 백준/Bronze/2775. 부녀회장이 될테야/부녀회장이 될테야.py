T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    f0 = list(range(1,n+1))
    for _ in range(k):
        for nn in range(1,n):
            f0[nn] = f0[nn-1] + f0[nn]
    print(f0[n-1])         
            
            