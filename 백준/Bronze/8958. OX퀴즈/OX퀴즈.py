N = int(input())
for _ in range(N):
    OX = input()
    score = 0
    consecutive = 0
    for ox in OX:
        if ox == 'O':
            consecutive += 1
            score += consecutive
        else:
            consecutive = 0
    print(score)