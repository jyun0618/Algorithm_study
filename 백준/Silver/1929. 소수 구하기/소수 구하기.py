import sys
input = sys.stdin.readline

M, N = map(int, input().split())
prime = [True] * (N - M + 1)  # M부터 N까지 소수 여부

for i in range(2, int(N ** 0.5) + 1):
    start = max(i * i, ((M + i - 1) // i) * i)  # M 이상에서 시작하는 i의 배수
    for j in range(start, N + 1, i):
        prime[j - M] = False

if M == 1:
    prime[0] = False  # 1은 소수가 아님

for idx, is_prime in enumerate(prime):
    if is_prime:
        print(M + idx)
