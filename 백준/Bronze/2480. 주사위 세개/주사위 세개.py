A, B, C = map(int, input().split())
if A == B == C:
    print(10000 + A*1000)
elif (A == B and A != C) or (A == C and A != B):
    print(1000 + A*100)
elif B == C and B != A:
    print(1000 + B*100)
else:
    print(max(A,B,C)*100)