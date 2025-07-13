N, K = map(int, input().split())
coins = []
count = 0
for _ in range(N):
    coin = int(input())
    if coin > K:
        break
    else:
        coins.append(coin)

count += K // coins[-1]
K -= coins[-1] * (K // coins[-1])

while True:
    if K == 0:
        break
    else:
        for idx, coin in enumerate(coins):
            if coin > K:
                coins = coins[:idx]
                break
        count += K // coins[-1]
        K -= coins[-1] * (K // coins[-1])

print(count)