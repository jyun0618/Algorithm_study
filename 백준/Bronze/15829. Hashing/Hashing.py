L = int(input())
seq = list(input())
import string
alphabet = list(string.ascii_lowercase)
h = 0
for l in range(L):
    for i in range(26):
        if seq[l] == alphabet[i]:
            h += (i+1)*31**l
print(h%1234567891)
    