isbn = input()
index = isbn.index('*')

total = 0
for i in range(13):
    if i == index:
        continue
    weight = 1 if i % 2 == 0 else 3
    total += weight * int(isbn[i])

for j in range(10):
    sum = total + (j * (1 if index % 2 == 0 else 3))
    if sum % 10 == 0:
        print(j)
        break