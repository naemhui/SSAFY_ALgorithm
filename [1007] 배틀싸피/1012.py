# 유기농 배추
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<M:
                # 새 좌표에 배추가 있으면(1) 그 좌표를 큐에 추가
                if arr[nx][ny] == 1:
                    queue.append((nx,ny))  # queue에 있다 = 해당 좌표는 탐색 대기 중
                    # 방문한 곳임을 표시
                    arr[nx][ny] = 0
    
    # queue가 비게 되면 while문 종료 후 return 실행
    return


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            # 배추가 있다면
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)