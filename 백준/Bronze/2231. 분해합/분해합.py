N = int(input())
for i in range(N):
    if N == sum(int(n) for n in str(i)) + i:
        answer = i
        break
    else: answer = 0
print(answer)