import string

def solution(s, skip, index):
    alpha = list(string.ascii_lowercase)

    # skip 문자 제거
    for a in skip:
        if a in alpha:
            alpha.remove(a)

    result = []

    for ch in s:
        cur_idx = alpha.index(ch)
        new_idx = (cur_idx + index) % len(alpha)
        result.append(alpha[new_idx])

    return ''.join(result)
