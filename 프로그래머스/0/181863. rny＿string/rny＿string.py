def solution(rny_string):
    answer = []
    for str in rny_string:
        if str == 'm':
            str = 'rn'
            answer.append(str)
        else:
            answer.append(str)
    return ''.join(answer)