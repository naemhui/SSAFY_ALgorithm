# 강사님쓰 뻬이보릿 코드 => push 하면서 방문 처리
# dfs처럼 처리는 안 되지만 stack에 한 번씩만 들어가는 장점
def dfs1(s):
    stack = []
    visited = [False] * (V+1)
    stack.append(s)
    visited[s] = True

    while stack:
        v = stack.pop()
        print(v)

        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for i in range(E):
    s, e = map(int, input().split())
    # s에서 갈 수 있는 정점 e 추가
    graph[s].append(e)
    # e 에서 갈 수 있는 정점 s 추가
    graph[e].append(s)

dfs1(1, V)