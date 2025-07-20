T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    Mfac = 1
    for m in range(1,M+1):
        Mfac *= m
    Nfac = 1
    for n in range(1,N+1):
        Nfac *= n
    MNfac = 1
    for n in range(1,M-N+1):
        MNfac *= n
    
    case = Mfac // (MNfac * Nfac)
    print(case)