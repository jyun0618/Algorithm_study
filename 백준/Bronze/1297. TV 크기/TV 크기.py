D, H, W = map(int, input().split())
rate = (D**2 / (H**2 + W**2)) ** 0.5
H = int(H*rate)
W = int(W*rate)

print(H, W)