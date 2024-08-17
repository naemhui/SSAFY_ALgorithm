def dfs1(s):
    stack = []
    visited = [False] * (V+1)
    stack.append(s)
    visited[s] = True

    while stack:
        v = stack.pop()
        if v == G:
            return 1
        # print(v)

        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        s, e = map(int, input().split())
        # s에서 갈 수 있는 정점 e 추가
        graph[s].append(e)
    
    S, G = map(int, input().split())

    print(f'#{tc} {dfs1(S)}')