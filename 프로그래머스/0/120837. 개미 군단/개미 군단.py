def solution(hp):
    answer = hp // 5
    if hp % 5 != 0:
        answer += (hp % 5) // 3
        if (hp % 5) % 3 != 0:
            answer += (hp % 5) % 3
    return answer