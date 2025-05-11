N = int(input())
factorial = 1
for i in range(1,N+1):
    factorial *= i

factorial = list(str(factorial))

zero = 0
for n in factorial[::-1]:
    if n == '0':
        zero += 1
    else:
        break

print(zero)