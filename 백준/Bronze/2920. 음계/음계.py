num = list(map(int, input().split()))
if all(num[i] < num[i+1] for i in range(7)):
    print('ascending')
elif all(num[i] > num[i+1] for i in range(7)):
    print('descending')
else:
    print('mixed')