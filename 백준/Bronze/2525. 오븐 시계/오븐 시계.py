A, B = map(int, input().split())
time = int(input())
if B + time >= 60:
    if A + (B+time)//60 > 23:
        print(A+(B+time)//60 - 24, (B+time)%60)
    else:
        print(A+(B+time)//60, (B+time)%60)
elif B + time < 60:
    print(A, B+time)