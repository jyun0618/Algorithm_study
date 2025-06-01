N = int(input())
cycle = 1
new = 10 * (N%10) + (N//10 + N%10)%10

while N != new:
    new = 10 * (new%10) + (new//10 + new%10)%10
    cycle += 1

print(cycle)