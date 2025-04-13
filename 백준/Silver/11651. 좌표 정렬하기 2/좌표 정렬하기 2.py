N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

sorted_indices = [i for i, _ in sorted(enumerate(zip(X, Y)), key=lambda x: (x[1][1], x[1][0]))]
for j in sorted_indices:   
    print(X[j], Y[j])