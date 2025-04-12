K = int(input())
total = []
for _ in range(K):
    N = int(input())
    if N != 0:
        total.append(N)
    else:
        if total: # total이 빈 리스트가 아닐 때 True
            total.pop()
print(sum(total))