## dequeue 이용한 방법
from collections import deque

# S: 시작 정점 번호
def bfs(S, E):
    visited = [0] * (V + 1)
    q = deque()
    q.append(S)
    visited[S] = 0

    while q:
        now = q.popleft()

        for x in G[now]:
            if not visited[x]:
                q.append(x)
                visited[x] = visited[now] + 1  # 거리 계산

                # 여기에서 확인: S에서 시작해, E를 방문하게 된다면
                if x == E:
                    return visited[x]
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        G[start].append(end)
        G[end].append(start)
    s, e = map(int, input().split())
    result = bfs(s, e)
    print(f'#{tc} {result}')


## 기본 - 인접리스트
# def bfs(s, e):
#     visited = [0] * (V + 1)
#     q = []
#     q.append(s)
#     visited[s] = 1
#
#     while q:
#         t = q.pop(0)
#
#         for w in adj_l[t]:
#             if visited[w] == 0:
#                 q.append(w)
#                 visited[w] = visited[t] + 1
#
#         if t == e:
#             return visited[t] - 1
#
#     return 0
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#
#     adj_l = [[] for _ in range(V + 1)]
#
#     for i in range(E):
#         start, end = map(int, input().split())
#         adj_l[start].append(end)
#         adj_l[end].append(start)
#
#     S, G = map(int, input().split())
#
#     result = bfs(S, G)
#
#     print(f"#{tc} {result}")
