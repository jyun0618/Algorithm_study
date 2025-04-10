while True:
    X = list(map(int, input().split()))
    if all(X[i] == 0 for i in range(3)):
        break
    X.sort()
    if X[2]**2 == X[0]**2 + X[1]**2:
        print('right')
    else:
        print('wrong')