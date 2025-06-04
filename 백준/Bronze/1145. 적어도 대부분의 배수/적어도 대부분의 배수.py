num = list(map(int, input().split()))

i = 1
while True:
    if sum(i % n == 0 for n in num) >= 3:
        print(i)
        break
    i += 1
