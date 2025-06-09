while True:
    N = input()
    if N == "0":
        break

    width = len(N) + 1
    for n in N:
        if n == '1':
            width += 2
        elif n == '0':
            width += 4
        else:
            width += 3


    print(int(width))
