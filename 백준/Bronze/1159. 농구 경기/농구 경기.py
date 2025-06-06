from collections import Counter

N = int(input())
name = [input() for _ in range(N)]
first_letters = Counter(n[0] for n in name)

result = sorted([ch for ch, cnt in first_letters.items() if cnt >= 5])

if result:
    print(''.join(result))
else:
    print('PREDAJA')