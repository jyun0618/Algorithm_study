total, subtract = map(int, input().split())
A = 0
B = 0
for a in range(total+1):
    if subtract == abs((total-a) - a):
        A = a
        B = total-a
        print(max(A,B), min(A,B))
        break
else:
    print(-1)