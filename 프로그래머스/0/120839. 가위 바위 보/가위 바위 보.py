def solution(rsp):
    answer = []
    for n in rsp:
        if n == '2':
            answer.append('0')
        elif n == '0':
            answer.append('5')
        else:
            answer.append('2')
    return ''.join(answer)