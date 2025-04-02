def solution(n):
    N=[]
    for value in str(n):
        N.append(int(value))
    answer=N[::-1]
    return answer