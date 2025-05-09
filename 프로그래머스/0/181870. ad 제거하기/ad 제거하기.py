def solution(strArr):
    strarr = []
    for ss in strArr:
        if 'ad' not in ss:
            strarr.append(ss)
    return strarr