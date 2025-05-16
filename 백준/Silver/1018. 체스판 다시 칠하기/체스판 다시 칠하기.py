N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

BW = []
for i in range(M-7):
    for j in range(N-7):
        Chess = [vec[i:i+8] for vec in board[j:j+8]]
        
        
        start_b = 0
        start_w = 0
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 0:
                    if Chess[x][y] != 'W':
                        start_w += 1
                    if Chess[x][y] != 'B':
                        start_b += 1

                else:
                    if Chess[x][y] != 'W':
                        start_b += 1
                    if Chess[x][y] != 'B':
                        start_w += 1
        BW.append(min(start_b, start_w))
              
print(min(BW))
            