# (0,0) 흰색
answer = 0
for i in range(8):
    row = list(input())
    cnt = 0
    for j in range(8):
        if (i + j)%2 == 0:
            if row[j] == 'F':
                cnt += 1
    answer += cnt
print(answer)