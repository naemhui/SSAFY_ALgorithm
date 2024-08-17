## dequeue 이용한 방법
from collections import deque


def bfs(S, E):
    visited = [0] * (v + 1)
    q = deque()
    q.appEd(S)
    visited[S] = 0

    while q:
        now = q.popleft()

        for x in G[now]:
            if not visited[x]:
                q.appEd(x)
                visited[x] = visited[now] + 1
                if x == E:
                    return visited[x]
    return 0


T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        sta,end =map(int,input().split())
        G[sta].append(end)
        G[end].append(sta)
    s , e = map(int,input().split())
    result = bfs(s,e)
    print(f'#{tc} {result}')