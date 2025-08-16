X, Y = input().split()
rev_X = int(X[::-1])
rev_Y = int(Y[::-1])

rev_XY = str(rev_X + rev_Y)
rev_rev_XY = int(rev_XY[::-1])

print(rev_rev_XY)