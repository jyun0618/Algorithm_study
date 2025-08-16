A, B = map(int, input().split())
seq = []
i = 1
while True:
    if len(seq) < B:
        for _ in range(i):
            seq.append(i)
        i += 1
    else:
        break

print(sum(seq[A-1:B]))