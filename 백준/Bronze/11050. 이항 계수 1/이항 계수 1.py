N, K = map(int, input().split())
NF = 1
NKF = 1
KF = 1
for n in range(1, N+1):
    NF *= n
for nk in range(1, N-K+1):
    NKF *= nk
for k in range(1, K+1):
    KF *= k        
print(int(NF/(NKF*KF)))