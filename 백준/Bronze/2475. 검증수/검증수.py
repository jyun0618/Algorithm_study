A = list(map(int, input().split()))
sum = 0
for i in range(len(A)):
    sum += A[i]**2
    
answer = sum % 10
print(answer)