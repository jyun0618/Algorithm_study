A, B = map(int, input().split())
a = (A%10)*100 + ((A//10)%10)*10 + A//100
b = (B%10)*100 + ((B//10)%10)*10 + B//100
print(max(a,b))