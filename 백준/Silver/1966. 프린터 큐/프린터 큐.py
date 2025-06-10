from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    queue = deque([(i, p) for i, p in enumerate(importance)])  # (index, priority)
    order = 0  # 출력 순서

    while queue:
        cur = queue.popleft()
        if any(cur[1] < doc[1] for doc in queue):
            queue.append(cur)  # 중요도 높은 문서가 있으면 뒤로
        else:
            order += 1
            if cur[0] == M:
                print(order)
                break
