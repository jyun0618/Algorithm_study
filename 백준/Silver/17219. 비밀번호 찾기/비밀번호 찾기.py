import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = {}
for _ in range(N):
    site, pwd = input().split()
    memo[site] = pwd

for _ in range(M):
    print(memo[input().strip()])