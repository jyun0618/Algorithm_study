def solution(my_string):
    num = []
    for str in my_string:
        try:
            int(str)
            num.append(int(str))
        except ValueError:
            pass
    return sum(num)