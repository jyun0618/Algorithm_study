N = int(input())
string = []
for _ in range(N):
    s = input()
    if s not in string:
        string.append(s)

string = sorted(string, key=lambda x: (len(x), x))
for s in string:
    print(s)