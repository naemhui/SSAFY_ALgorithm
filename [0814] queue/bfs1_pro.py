from collections import deque
'''
정점의 개수 : V, 간선의 개수 E
V = 7, E = 8
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

# G : 그래프 정보(인접리스트 OR 인접 행렬)
# V : 시작 정점 번호(탐색 시작 위치)
# N : 정점의 개수

def bfs(G, v, N):
    # 중복 방문 방지를 위한 방문 배열 필요
    visited = [0] * (N+1)
    # 내가 다음에 방문할 정점을 기억할 큐
    q = deque()  # 빈 큐를 만들 때는 deque. 근데 이미 만들어놓은 리스트가 있다면 deque([1,2,3])
    # 큐에 시작정점을 넣은 상태로 탐색 시작
    q.append(v)
    visited[v] = 1
    # 큐가 빌 때까지 계속 탐색 == 큐 안에 방문할 곳이 남았으면 계속 탐색
    while q:
        # 큐에서 방문할 곳 하나 꺼내오기
        now = q.popleft()

        #############
        # now에서 할 일 처리
        print(now, end=" ")
        #############

        # 현재 정점 now에서 연결된 모든 정점 next 확인
        for next in G[now]:
            # next 정점을 이전에 방문한 적이 없으면 다음 방문 예약
            if not visited[next]:
                # 다음에 방문하기 위해 큐에 넣어두기
                q.append(next)
                # 중복 방문 처리
                # next까지의 거리 = now까지의 거리 + 1
                visited[next] = visited[now]+1  # 거리 계산까지 한 번에


V, E = map(int, input().split())
# 그래프를 표현하는 방법은 인접리스트와 인접행렬이 있다
G = [[] for _ in range(V+1)]  # 인접리스트로 그래프 표현
for i in range(E):
    start, end = map(int, input().split())
    G[start].append(end)
    G[end].append(start)  # 무향 그래프

bfs(G, 1, V)
