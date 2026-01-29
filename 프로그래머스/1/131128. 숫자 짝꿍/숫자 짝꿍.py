def solution(X, Y):
    answer = []

    X = list(map(int, str(X)))
    Y = list(map(int, str(Y)))

    for d in range(9, -1, -1):
        cnt = min(X.count(d), Y.count(d))
        answer.extend([str(d)] * cnt)

    if not answer:
        return "-1"

    if answer[0] == "0":
        return "0"

    return ''.join(answer)
