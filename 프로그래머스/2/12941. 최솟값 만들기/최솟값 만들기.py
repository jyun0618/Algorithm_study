def solution(A,B):
    cumsum=0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        cumsum += A[i]*B[i]
    return cumsum
        
        