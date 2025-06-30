import sys
import math

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    opinions = [int(sys.stdin.readline()) for _ in range(n)]
    opinions.sort()
    
    cut = math.floor(n * 0.15 + 0.5)
    trimmed = opinions[cut:n - cut]
    
    if not trimmed:
        print(0)
    else:
        print(math.floor(sum(trimmed) / len(trimmed) + 0.5))
