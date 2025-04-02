N = int(input())
A = list(map(int, input().split()))
V = int(input())

print(sum(1 for a in A if a==V))