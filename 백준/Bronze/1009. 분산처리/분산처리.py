T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    num = []
    for i in range(1,b+1):
        if (a**i)%10 not in num:
            num.append((a**i)%10)
        else:
            break
    idx = (b-1)%len(num)
    print(10 if num[idx]==0 else num[idx])