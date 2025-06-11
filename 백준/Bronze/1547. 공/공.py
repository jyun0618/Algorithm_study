M = int(input())
# 컵 위치: index는 위치(0,1,2), 값은 컵 번호
position = [1, 2, 3]

# 공은 처음에 1번 컵 아래 → 1번 컵의 위치(인덱스)를 추적
ball_pos = position.index(1)

for _ in range(M):
    X, Y = map(int, input().split())
    
    # 각각의 컵 번호 X, Y의 현재 위치를 구함
    x_index = position.index(X)
    y_index = position.index(Y)
    
    # 컵의 위치를 바꿈
    position[x_index], position[y_index] = position[y_index], position[x_index]

# 공이 들어있는 컵 번호 = 현재 공이 위치한 곳의 컵 번호
print(position[ball_pos])
