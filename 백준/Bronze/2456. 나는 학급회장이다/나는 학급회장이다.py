import sys

N = int(sys.stdin.readline().strip())
tot = [0, 0, 0]   # 총점
c3  = [0, 0, 0]   # 3점 횟수
c2  = [0, 0, 0]   # 2점 횟수

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    votes = [a, b, c]
    for i, v in enumerate(votes):
        tot[i] += v
        if v == 3: c3[i] += 1
        elif v == 2: c2[i] += 1

# 각 후보의 비교용 튜플 (총점, 3점 개수, 2점 개수)
metrics = [(tot[i], c3[i], c2[i]) for i in range(3)]
best_idx = max(range(3), key=lambda i: metrics[i])
best_metric = metrics[best_idx]

# 같은 metric을 가진 후보가 여러 명이면 회장 결정 불가
if metrics.count(best_metric) > 1:
    print(0, max(tot))
else:
    print(best_idx + 1, tot[best_idx])