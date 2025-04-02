def solution(n):
    result=[]
    for x in range(1,n):
        if n%x==1:
            result.append(x)
    answer=min(result)
    return answer