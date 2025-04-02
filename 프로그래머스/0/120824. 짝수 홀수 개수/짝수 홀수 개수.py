def solution(num_list):
    even = []
    odd = []
    for value in num_list:
        if value%2==0:
            even.append(value)
        else:
            odd.append(value)
    answer=(len(even),len(odd))
    return answer