from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()
print(round(sum(nums)/N))  # 산술평균
print(nums[N//2])  # 중앙값

# 최빈값
freq = Counter(nums)
most_common = freq.most_common()
max_freq = most_common[0][1]
modes = [num for num, count in most_common if count == max_freq]
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])  # 최빈값

# 범위
print(nums[-1] - nums[0])
