from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {x: y for x, y in zip(want, number)}
    for i in range(0,len(discount)-8):
        if dic==Counter(discount[i:i+10]):
            answer+=1
    return answer