def solution(n):
    answer=0
    for i in range(1,n+1):
        cumsum=0
        j=i
        while cumsum<n:
            cumsum+=j
            j+=1
            if cumsum==n:
                answer+=1
    return answer