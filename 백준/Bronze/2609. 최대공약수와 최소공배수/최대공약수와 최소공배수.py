A, B = map(int, input().split())
import math
gcd = math.gcd(A, B)
lcm = A * B // gcd

print(gcd)
print(lcm)
