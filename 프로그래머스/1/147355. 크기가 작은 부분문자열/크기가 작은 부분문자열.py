def solution(t, p):
    result=[]
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)])<= int(p):
            result.append(t[i:i+len(p)])
    answer=len(result)
    return answer