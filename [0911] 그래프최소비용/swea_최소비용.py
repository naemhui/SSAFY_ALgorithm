from heapq import heappush, heappop

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dijkstra():
    # (가중치, 행번호, 열번호)
    q = [(0, 0, 0)]
    # 시작 지점의 가중치는 0으로
    distance[0][0] = 0

    while q:
        # w(가중치) r,c(행번호 열번호)
        w, r, c = heappop(q)

        # 방금 꺼내온 r,c까지의 거리 w가
        # 이전에 내가 계산해놓은 r,c까지의 거리보다 크면 계산 X
        if distance[r][c] < w:
            continue

        # 현재 노드와 연결되어 있는 다른 인접한 노드 확인
        # 2차원 배열 => 상하좌우
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 계산한 위치가 유효한 위치면
            if 0 <= nr <N and 0 <= nc < N:
                # nr,nc가 이동 가능한 위치
                # 연료를 1 소모해서 갈 수 있는데
                # nr,nc의 높이가 더 높으면 추가 소비
                h_diff = 0
                if arr[nr][nc] > arr[r][c]:
                    h_diff = arr[nr][nc] - arr[r][c]

                # nr,nc까지 이동하는 데에 사용한 연료량
                # r,c까지 이동하는 데 사용한 연료 + 기본 사용량 + 높이 차이
                # 이거랑 내가 이전에 계산해놓은 nr,nc까지 이동하는 데 사용한 연료량과 비교
                # 그 중 최솟값 선택(지금 계산한 값이 더 작으면 갱신)
                cost = distance[r][c] + 1 + h_diff

                # 내가 방금 계산한 비용이 이전에 계산했던 것보다 작으면 갱신
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    # 갱신이 일어났을 때 큐에 추가
                    heappush(q, (cost, nr, nc))


# 다익스트라 알고리즘 응용
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # (0,0) ~ (N-1,N-1)로 가는 데에 최단 거리

    # distance[i] : 시작지점부터 i까지 최단 거리
    # distance[r][c] : 시작지점부터 (r,c)까지 최단 거리
    distance = [[1e9]*N for _ in range(N)]

    # 다익스트라 알고리즘 실행
    dijkstra()

    # (N-1, N-1)까지의 최소 거리
    print(f'#{tc} {distance[N-1][N-1]}')