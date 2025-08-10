N, M = map(int, input().split())
A = list(map(int, input().split()))  # 박스 용량
B = list(map(int, input().split()))  # 책의 크기

waste = 0
box_idx = 0  # 현재 박스 인덱스

for book in B:
    if A[box_idx] >= book:
        # 책 넣기
        A[box_idx] -= book
    else:
        # 현재 박스 잔여 용량 버림
        waste += A[box_idx]
        box_idx += 1
        A[box_idx] -= book

# 책을 다 넣은 후 남은 박스 잔여 용량 모두 더하기
waste += sum(A[box_idx:])

print(waste)