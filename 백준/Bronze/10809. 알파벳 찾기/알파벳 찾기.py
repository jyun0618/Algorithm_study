import string
S = input()
for s in string.ascii_lowercase:
    try:
        print(S.index(s), end=' ')
    except ValueError:
        print(-1, end=' ')