max_val = -1
max_row = 0
max_col = 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max_val:
            max_val = row[j]
            max_row = i
            max_col = j

print(max_val)
print(max_row + 1, max_col + 1)
