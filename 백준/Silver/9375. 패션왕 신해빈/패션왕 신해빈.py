N = int(input())
for _ in range(N):
    n = int(input())
    clothes = {}
    for _ in range(n):
        _, type = input().split()
        clothes[type] = clothes.get(type, 0) + 1
    case = 1
    for count in clothes.values():
        case *= count + 1
    print(case - 1)
    
    