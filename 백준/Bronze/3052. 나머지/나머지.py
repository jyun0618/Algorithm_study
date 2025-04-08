remain = []
for _ in range(10):
    N = int(input())
    remain.append(N % 42)

print(len(set(remain)))