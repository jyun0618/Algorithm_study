A, B, C = map(int, input().split())
D = int(input())

B += D // 60
C += D % 60

if C >= 60:
    B += C // 60
    C = C % 60

if B >= 60:
    A += B // 60
    B = B % 60

if A > 23:
    A = A % 24

print(A, B, C)