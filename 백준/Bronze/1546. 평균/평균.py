N = int(input())
score = list(map(int, input().split()))
normalized = [s/max(score)*100 for s in score]
print(sum(normalized)/N)