def solution(num_list):
    odd = []
    even = []
    for i in range(len(num_list)):
        if num_list[i] % 2 != 0:
            odd.append(num_list[i])
        else:
            even.append(num_list[i])
    answer = int(''.join(map(str, odd))) + int(''.join(map(str, even)))
    return answer