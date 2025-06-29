A, B = map(int, input().split())
if A%4 == 0:
    Aa = A//4
    Ab = 4
else:
    Aa = A//4 + 1
    Ab = A%4

if B%4 == 0:
    Ba = B//4
    Bb = 4
else:
    Ba = B//4 + 1
    Bb = B%4

# 11: 2,3
# 33: 8,1
# 24: 6,0

dist = abs(Aa-Ba) + abs(Ab-Bb)
print(dist)