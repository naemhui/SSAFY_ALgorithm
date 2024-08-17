# ```
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# ```

def DFS(s, v):  # s시작정점, V정점개수(마지막정렬)
    visited = [0] *(V+1) # 방문한 정점 표시
    stack = [] # 스택 생성이 필요
    print(s)  # 개수

    visited[s] = 1  # 시작정점 방문 표시
    v = s
    while True:
        for w in adjL[v]:  # v에 인접하고 방문 안 한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # push(v) 현재 정점을 push 하고
                v = w  # w에 방문
                print(v)

                visited[w]  # w에 방문 표시
                break  # for w, v부터 다시 탐색
        else:   # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
            if stack:  # 이전 갈림길을 스택에서 꺼내서
                # append pop일 경우니까 if stack(top이면 if top > -1)
                v = stack.pop()
            else:
                break  # while True에 대한 break



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[]for _ in V+1]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[1*2+1]  # 이렇게 하면 한 쌍씩 읽을 수 있음
        adjL[v1].append(v2)
        adjL[v2].append(v1)
        adjL.append(v2)

    print(DFS(1, V))