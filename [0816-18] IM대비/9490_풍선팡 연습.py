# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c, N, M):
    return 0<=r<N and 0<=c<M

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for r in range(N):
        for c in range(M):
            sum_v = arr[r][c]

            for d in range(4):
                for k in range(arr[r][c]):
                    nr = r + dr[d]*(k+1)
                    nc = c + dc[d]*(k+1)

                    if is_valid(nr, nc, N, M):
                        # r, c = nr, nc
                        sum_v += arr[nr][nc]

            if sum_v > max_v:
                max_v = sum_v
    
    print(f'#{tc} {max_v}')