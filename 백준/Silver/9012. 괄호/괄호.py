T = int(input())
for _ in range(T):
    PS = input()
    if PS.count('(') != PS.count(')'):
        print('NO')
    else:
        for i in range(len(PS)):
            if PS[i] == ')':
                if PS[:i+1].count(')') > PS[:i+1].count('('):
                    print('NO')
                    break
            else:
                pass
        else:
            print('YES')