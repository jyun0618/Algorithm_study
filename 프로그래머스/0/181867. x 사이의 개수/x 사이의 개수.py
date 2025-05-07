def solution(myString):
    answer = []
    length = []
    for str in myString:
        if str == 'x':
            length.append(len(answer))
            answer = []
        else:
            answer.append(str)
    length.append(len(answer))
    return length