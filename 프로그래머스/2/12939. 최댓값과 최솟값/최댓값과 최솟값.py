def solution(s):
    s=s.split()
    result=[]
    for value in s:
        result.append(int(value))
    answer=' '.join([str(min(result)),str(max(result))])
    return answer