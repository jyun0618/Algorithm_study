def solution(n):
    result=[]
    for value in str(n):
        result.append(int(value))
    answer=sum(result)
    return answer