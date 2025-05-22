x, y, w, h = map(int, input().split())
minvalue = min(abs(x-w), abs(y-h),x,y)
print(minvalue)