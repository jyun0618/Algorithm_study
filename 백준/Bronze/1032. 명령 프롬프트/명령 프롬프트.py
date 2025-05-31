N = int(input())
file = list(input())
length = len(file)
for _ in range(N-1):
    file2 = list(input())
    for i in range(length):
        if file[i] != file2[i]:
            file[i] = '?'
            
print(''.join(file))  