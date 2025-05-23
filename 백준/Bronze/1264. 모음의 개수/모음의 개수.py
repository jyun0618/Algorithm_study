while True:
    statement = input().lower()
    if statement == '#':
        break
    count = 0
    count += statement.count('a')
    count += statement.count('e')
    count += statement.count('i')
    count += statement.count('o')
    count += statement.count('u')
    print(count)