def solution(n):
    strn = str(n)
    answer=0
    for digit in strn:
        answer+=int(digit)
    return answer