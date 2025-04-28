while True:
    N = input()
    if N == '0':
        break
    print('yes' if N == N[::-1] else 'no')
