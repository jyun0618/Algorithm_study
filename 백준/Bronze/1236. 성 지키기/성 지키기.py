N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]

rows_without_guard = sum(1 for row in castle if all(cell == '.' for cell in row))

cols_without_guard = 0
for col in range(M):
    if all(castle[row][col] == '.' for row in range(N)):
        cols_without_guard += 1

print(max(rows_without_guard, cols_without_guard))
