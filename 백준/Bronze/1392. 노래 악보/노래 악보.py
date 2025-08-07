N, Q = map(int, input().split())

Ti = []
for n in range(1, N+1):
    Bi = int(input())
    for _ in range(Bi):
        Ti.append(n)

for _ in range(Q):
    TQ = int(input())
    print(Ti[TQ])