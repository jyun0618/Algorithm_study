def solution(array, height):
    result=[]
    for value in array:
        if value>height:
            result.append(value)
    answer=len(result)
    return answer