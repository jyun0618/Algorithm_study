def solution(s1, s2):
    result=[]
    for value in s1:
        if value in s2:
            result.append(value)
    answer=len(result)
    return answer