def solution(n):
    result=[]
    for value in str(n):
        result.append(value)
    result.sort(reverse=True)
    answer = int(''.join(result))
    return answer