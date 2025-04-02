import math

def solution(n):
    root=math.sqrt(n)
    if root.is_integer()==1:
        answer=1
    else:
        answer=2
    return answer