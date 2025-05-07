def solution(n):
    if n%2!=0:
        summ = 0
        for i in range((n+1)//2):
            summ += 2*i + 1
    else:
        summ = 0
        for j in range(1,n//2+1):
            summ += (2*j)**2
    return summ