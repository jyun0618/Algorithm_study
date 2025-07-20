EngName = input()
N = int(input())

win = []
for _ in range(N):
    Team = input()
    L = EngName.count('L') + Team.count('L')
    O = EngName.count('O') + Team.count('O')
    V = EngName.count('V') + Team.count('V')
    E = EngName.count('E') + Team.count('E')
    win_prob = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    win.append((win_prob, Team))

win = sorted(win, key = lambda x: (-x[0], x[1]))
print(win[0][1])