def solution(my_string, letter):
    result=[]
    for value in my_string:
        if value!=letter:
            result.append(value)
    answer=''.join(result)
    return answer