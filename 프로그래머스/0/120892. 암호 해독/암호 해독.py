def solution(cipher, code):
    str = list(cipher)
    answer = []
    for i in range(1, len(str)//code+1):
        answer.append(str[code*i-1])
    return ''.join(answer)