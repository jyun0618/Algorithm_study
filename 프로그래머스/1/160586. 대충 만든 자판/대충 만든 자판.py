def solution(keymap, targets):
    answer = []
    
    for t in targets:
        total = 0
        for ch in t:
            candidates = [key.index(ch) + 1 for key in keymap if ch in key]
            if not candidates:
                total = -1
                break
            total += min(candidates)
        answer.append(total)
    
    return answer
