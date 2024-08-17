# 상하좌우 순서
dr = [0, 1, 0, -1]  # 행
dc = [1, 0, -1, 0]  # 열

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    d = 0  # 방향 인덱스!
    r, c = 0, 0  # 출발 위치

    for i in range(1, N*N+1):
        snail[r][c] = i  # 달팽이 1부터 채워짐

        nr = r + dr[d]  # 다음 행 인덱스
        nc = c + dc[d]  # 다음 열 인덱스

        # 유효 인덱스 검사
        if 0 <= nr <N and 0 <= nc < N and snail[nr][nc] == 0: # 다음 위치 유효하면
            r, c = nr, nc  # -> 그대로 진행

        else:
            d = d + 1 if d < 3 else 0  # 유효한 인덱스가 되도록(d는 0, 1, 2, 3)
            r = r + dr[d]
            c = c + dc[d]

    print(f'#{tc}')

    for i in range(N):
        print(*snail[i])