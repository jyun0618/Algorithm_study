def solution(numbers):
    mul = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            mul.append(numbers[i]*numbers[j])
    return max(mul)