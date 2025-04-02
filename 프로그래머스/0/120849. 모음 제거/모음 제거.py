def solution(my_string):
    result = []
    for value in my_string:
        if value not in ('a','e','i','o','u'):
            result.append(value)
    answer=''.join(result)
    return answer