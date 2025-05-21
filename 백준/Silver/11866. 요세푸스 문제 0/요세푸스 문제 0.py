N, K = map(int, input().split())

P = []
n = list(range(1,N+1))
index = 0

while n: # n 리스트가 비어있지 않을 때까지 반복
    index = (index + K - 1) % len(n)
    P.append(str(n.pop(index)))
      
print('<' + ', '.join(P) + '>')        