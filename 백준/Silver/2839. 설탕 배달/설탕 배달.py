N = int(input())

if N % 5 == 0:
    print(N//5)

else:
    for i in range(N//5,-1,-1):
        if (N - (5 * i)) % 3 == 0:
            print(i + (N - (5 * i))//3)
            break
    else:
        print(-1)