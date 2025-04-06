X = []
for _ in range(9):
    X.append(int(input()))
print(max(X))
for i in range(9):
    if X[i] == max(X):
        print(i+1)