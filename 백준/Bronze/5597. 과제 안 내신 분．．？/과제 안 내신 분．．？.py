A = list(range(1,31))
for _ in range(28):
    a = int(input())
    A.remove(a)
print(min(A))
print(max(A))    
    