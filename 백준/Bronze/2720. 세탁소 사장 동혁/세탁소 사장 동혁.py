T = int(input())
for _ in range(T):
    C = int(input())
    
    a = C//25
    C -= 25*(C//25)
    
    b = C//10
    C -= 10*(C//10)
    
    c = C//5
    C -= 5*(C//5)
    
    d = C//1
    print(a,b,c,d)