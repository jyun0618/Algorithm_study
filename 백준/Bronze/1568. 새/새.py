N = int(input())
K = 1
sec = 0
while N > 0:
    if N < K:
        K = 1
    else:
        N -= K
        sec += 1
        if N == 0:
            print(sec)
            break
        else:
            K += 1