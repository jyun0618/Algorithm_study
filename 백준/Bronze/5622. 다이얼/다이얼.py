alphabet = input()
second = 0
for n in alphabet:
    if n in ('A','B','C'):
        second += 3
    elif n in ('D','E','F'):
        second += 4
    elif n in ('G','H','I'):
        second += 5
    elif n in ('J','K','L'):
        second += 6
    elif n in ('M','N','O'):
        second += 7
    elif n in ('P','Q','R','S'):
        second += 8
    elif n in ('T','U','V'):
        second += 9
    elif n in ('W','X','Y','Z'):
        second += 10
    else:
        second += 1
print(second)