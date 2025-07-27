N, M = map(int, input().split())

packs = []
singles = []
for _ in range(M):
    pack, single = map(int, input().split())
    packs.append(pack)
    singles.append(single)

p = min(packs)
s = min(singles)

money = []
for i in range(N//6+1):
    money.append(i * p + (N-6*i) * s)
    money.append((N//6+1)*p)
print(min(money))
    