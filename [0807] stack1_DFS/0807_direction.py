def dfs1(s):
    stack = []
    visited = [False] * 100
    stack.append(s)
    visited[s] = True

    while stack:
        v = stack.pop()
        if v == 99:
            return 1

        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True
    return 0

for TC in range(10):
    T, E = map(int, input().split())
    graph = [[] for _ in range(100)]

    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        v1, v2 = data[i], data[i+1]
    # s에서 갈 수 있는 정점 e 추가
        graph[v1].append(v2)

    print(f'#{TC+1} {dfs1(0)}')