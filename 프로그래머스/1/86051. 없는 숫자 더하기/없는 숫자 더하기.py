def solution(numbers):
    answer = 0
    for n in range(0,10):
        if n not in numbers:
            answer += n
    return answer