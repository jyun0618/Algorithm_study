def solution(my_string):
    num = []
    for str in my_string:
        try:
            num.append(int(str))
        except ValueError:
            pass
    num.sort()
    return num