# 22683. 나무 베기
from collections import deque

def bfs():
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 시작위치, 방향(현재 rc카), 나무 벤 횟수, 조작 횟수
    q = deque([(start[0], start[0], 0, 0, 0)])
    # 방문 위치와 상태 저장
    visited = set([(start[0], start[1], 0, 0)])

    while q:
        r, c, d, cut, steps = q.popleft()

        # 현재 위치 = 목표 위치라면 steps 반환
        if (r, c) == end:
            return steps

        # 앞으로 전진
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:  # 필드 범위 안에 있으면
            # 이동 가능한 땅이면 큐에 추가, 방문 기록
            if arr[nr][nc] in 'GXY' and (nr, nc, d, cut) not in visited:
                q.append((nr, nc, d, cut, steps+1))
                visited.add((nr, nc, d, cut))

            # 이동 위치에 나무가 있고 횟수(K)가 남아있다면 
            # 나무 베고(cut+1) 큐에 추가
            # 나무 벴으면 횟수 기록하고 새로운 상태로 이동
            elif arr[nr][nc] == 'T' and cut < K and (nr, nc, d, cut+1) not in visited:
                q.append((nr, nc, d, cut+1, steps+1))
                visited.add((nr, nc, cut+1, d))

        # 좌회전 or 우회전
        # d-1: 좌회전, d+1: 우회전
        for direct in ((d - 1) % 4, (d + 1) % 4):
            if (r, c, direct, cut) not in visited:
                q.append((r, c, direct, cut, steps+1))
                visited.add((r, c, direct, cut))

    # 목표 위치에 도달하지 못하면 -1 반환
    return -1


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 시작 위치와 도착 위치 찾기
    start = end = None
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)
            
            elif arr[i][j] == 'Y':
                end = (i, j)
    
    print(f'#{tc} {bfs()}')