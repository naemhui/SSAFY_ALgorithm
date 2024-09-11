# '''
# N,E : 0~N까지의 번호(노드는 N+1개), 도로(간선 수)
# 0번 ~ N번까지 이동하는 데 걸리는 최소한의 거리 출력
# '''

import heapq

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정 (도달할 수 없을 때의 거리로 사용)

# 다익스트라 알고리즘 함수
def dijkstra(start, n, graph):
    # 시작 지점에서 각 노드까지의 거리를 저장할 리스트. 처음엔 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    
    # 우선순위 큐를 이용해 최단 거리를 계산 (파이썬의 heapq는 최소 힙)
    pq = []
    # 시작 노드의 거리는 0이므로 (0, 시작노드)를 우선순위 큐에 삽입
    heapq.heappush(pq, (0, start))
    distance[start] = 0  # 시작 지점에서 자신까지의 거리는 당연히 0

    # 큐가 빌 때까지 반복
    while pq:
        # 가장 거리가 짧은 노드를 꺼내자
        dist, now = heapq.heappop(pq)

        # 현재 노드가 이미 처리된 적이 있는 노드면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next in graph[now]:
            next_node, cost = next  # next_node는 다음으로 이동할 노드, cost는 그 노드까지의 거리
            new_cost = dist + cost  # 현재까지의 누적 거리(dist) + 다음 노드까지의 거리(cost)

            # 만약 새로운 비용이 현재 저장된 거리보다 더 짧다면
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost  # 더 짧은 거리로 업데이트
                heapq.heappush(pq, (new_cost, next_node))  # 우선순위 큐에 갱신된 정보를 삽입
    
    return distance  # 시작 노드에서 모든 노드로 가는 최단 거리 정보를 반환


T = int(input())

for tc in range(1, T + 1):
    # N: 마지막 연결지점 번호 (노드 번호), E: 도로의 개수 (간선의 개수)
    N, E = map(int, input().split())
    
    # 각 연결 지점에 대한 그래프 정보를 저장할 리스트 (인접 리스트)
    graph = [[] for _ in range(N + 1)]

    # 도로 정보 입력받기 (시작점 s, 끝점 e, 구간 거리 w)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))  # s에서 e로 가는 구간의 거리는 w

    # 다익스트라 알고리즘 실행(0번 지점에서 N번 지점까지의 최단 거리 구하기)
    distance = dijkstra(0, N, graph)

    # N번 지점까지의 최단 거리 결과를 출력
    result = distance[N]
    # 만약 N번 지점까지 도달할 수 없는 경우는 INF로 처리
    if result == INF:
        print(f"#{tc} INF")
    else:
        print(f"#{tc} {result}")

# from heapq import heappush, heappop


# def prim(start):
#     heap = list()
#     MST = [0] * (V+1)  # visited랑 똑같다

#     # 최소 비용 합계
#     sum_weight = 0

#     # 힙에서 관리해야 할 데이터
#     # 가중치, 정점 정보
#     # heappush(heap, (start, 0))  # 정점 가중치 -> 정점번호를 기준으로 정렬되기 때문에 안됨
#     heappush(heap, (0, start))  # 시작점은 가중치가 0이다

#     while heap:
#         weight, v = heappop(heap)  # 현재 시점에서 가중치가 가장 작은 정점이 pop

#         # 이미 방문한 지점이면 통과
#         if MST[v]:
#             continue

#         # 방문 처리
#         MST[v] = 1
#         # 누적합 추가
#         sum_weight += weight

#         # 갈수 있는 노드를 보면서
#         for next in range(V):
#             # 갈 수 없는 지점이면 continue
#             if graph[v][next] == 0:
#                 continue

#             # 이미 방문한 지점이면 continue
#             if MST[next]:
#                 continue

#             heappush(heap, (graph[v][next], next))

#     return sum_weight

# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     graph = [[0] * (V+1) for _ in range(V+1)]
#     for _ in range(E):
#         u, v, w = map(int, input().split())
#         graph[u][v] = w
#         graph[v][u] = w

#     result = prim(0)
#     print(f'#{tc} {result}')